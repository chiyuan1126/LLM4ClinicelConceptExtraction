import pandas as pd
import re
from io import StringIO


def clean_datetime_strings(line):
    # Remove or replace unrecognized timezone strings (e.g., "BLOOD", "URINE")
    # Replace with an empty string or another placeholder if needed
    return re.sub(r'\b(BLOOD|URINE)\b', '', line)


def extract_bio(text):
    if not isinstance(text, str):
        return []
    tags = []
    pattern = re.compile(r'(</?[^>]+>)')
    parts = pattern.split(text)
    current_tag = 'O'
    for part in parts:
        if part.startswith('<') and part.endswith('>'):
            if '/' not in part:
                current_tag = f'B-{part[1:-1]}'
            else:
                current_tag = 'O'
        else:
            words = re.findall(r"[\w']+|[.,!?;]", part)
            for word in words:
                tags.append((word, current_tag))
                if current_tag.startswith('B-'):
                    current_tag = current_tag.replace('B-', 'I-')
    return tags


def process_data(input_file, output_file):
    # Load NDJSON file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Clean lines to remove unrecognized timezone strings
    cleaned_lines = [clean_datetime_strings(line) for line in lines]

    bio_data = []
    skipped_lines = 0  # Counter for skipped lines

    for line_number, line in enumerate(cleaned_lines, start=1):
        try:
            # Convert each line to a pandas Series, skip if it cannot be parsed
            item = pd.read_json(StringIO(line), typ='series')

            # Check if 'answer' and 'predict' columns exist
            if 'answer' not in item or 'predict' not in item:
                print(f"Skipping line {line_number} due to missing 'answer' or 'predict' fields.")
                skipped_lines += 1
                continue

            # Try to convert 'answer' and 'predict' to strings
            try:
                answer_text = str(item['answer'])
                predict_text = str(item['predict'])
            except Exception as e:
                print(f"Skipping line {line_number} due to conversion error in 'answer' or 'predict': {e}")
                skipped_lines += 1
                continue

            # Extract BIO tags from 'answer' and 'predict' fields
            answer_tags = extract_bio(answer_text)
            predict_tags = extract_bio(predict_text)

            for (a_word, a_tag), (_, p_tag) in zip(answer_tags, predict_tags):
                bio_data.append({'answer': a_word, 'answer_tag': a_tag, 'predict_tag': p_tag})
        except ValueError as e:
            print(f"Skipping line {line_number} due to JSON parsing error: {e}")
            skipped_lines += 1
        except Exception as e:
            print(f"Skipping line {line_number} due to unexpected error: {e}")
            skipped_lines += 1

    # Convert bio_data to DataFrame
    df_corrected = pd.DataFrame(bio_data)

    separated_data = []
    previous_answer = None

    for index, row in df_corrected.iterrows():
        if previous_answer is not None:
            if previous_answer[-1] == '.' and row['answer'][0].isupper():
                separated_data.append({'answer': '', 'answer_tag': '', 'predict_tag': ''})
        separated_data.append(row.to_dict())
        previous_answer = row['answer']

    separated_df_corrected = pd.DataFrame(separated_data)
    separated_df_corrected.to_csv(output_file, sep=' ', index=False, header=False)

    # Ensure blank lines are completely blank (no spaces)
    with open(output_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            if line.strip() == '':
                f.write('\n')
            else:
                f.write(line)

    # Remove lines with unexpected number of fields
    with open(output_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            if len(line.split()) == 3 or line.strip() == '':
                f.write(line)

    # Output the number of skipped lines
    print(f"Total skipped lines: {skipped_lines}")


if __name__ == "__main__":
    input_file = "output/Mistral-7B-Instruct-v0.2/new_Mistral_7b_train_i2b2_2010+i2b2_2012_test_i2b2_2010_result.txt"
    output_file = "output/Mistral-7B-Instruct-v0.2/new_Mistral_7b_train_i2b2_2010+i2b2_2012_test_i2b2_2010_result_BIO.txt"
    process_data(input_file, output_file)

import json


def extract_entities(text, labels):
    entities = []
    current_entity_type = None
    current_entity_text = None
    current_entity_start = None

    for i, (word, label) in enumerate(zip(text, labels)):
        if label.startswith('B-'):
            if current_entity_type is not None and current_entity_text is not None:
                entities.append((current_entity_text, current_entity_type, current_entity_start, i - 1))
            current_entity_type = label.split('-')[1]
            current_entity_text = word
            current_entity_start = i
        elif label.startswith('I-'):
            if current_entity_type is not None and current_entity_text is not None:
                current_entity_text += ' ' + word
        else:
            if current_entity_type is not None and current_entity_text is not None:
                entities.append((current_entity_text, current_entity_type, current_entity_start, i - 1))
            current_entity_type = None
            current_entity_text = None

    if current_entity_type is not None and current_entity_text is not None:
        entities.append((current_entity_text, current_entity_type, current_entity_start, len(text) - 1))

    return entities


def process_input_file(input_file):
    data = []
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            json_data = json.loads(line)
            text = json_data["text"]
            labels = json_data["labels"]
            entities = extract_entities(text, labels)

            output_text = ' '.join(text)
            for entity_text, entity_type, start, end in entities:
                output_text = output_text.replace(entity_text, f'<{entity_type}>{entity_text}</{entity_type}>')

            adjusted_entities = {}
            for entity_text, entity_type, start, end in entities:
                if entity_type not in adjusted_entities:
                    adjusted_entities[entity_type] = {}
                adjusted_entities[entity_type][entity_text] = [start, end]

            data.append({"text": ' '.join(text), "labels": adjusted_entities, "output": output_text})
    return data


def process_output_file(output_file, data):
    with open(output_file, 'w', encoding='utf-8') as file:
        for entry in data:
            file.write(json.dumps(entry, ensure_ascii=False) + '\n')


if __name__ == "__main__":
    input_file_path = "data/AggregationCorpus/SentenceData/i2b2-2010+Llama3-8b生成i2b2-2010_200%/train_processed.txt"
    output_file_path = "data/AggregationCorpus/SentenceData/i2b2-2010+Llama3-8b生成i2b2-2010_200%/train_processed.json"

    input_data = process_input_file(input_file_path)
    process_output_file(output_file_path, input_data)

    print("Processing complete. Output written to train_processed.json.")

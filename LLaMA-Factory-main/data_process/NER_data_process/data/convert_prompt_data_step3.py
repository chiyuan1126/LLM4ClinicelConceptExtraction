import json


def convert_ner_cluener_prompt4(inputfile, outputfile):
    maxlen = 0
    max_source = 0
    max_target = 0
    data = []

    with open(inputfile, 'r', encoding='utf-8') as f:
        for line in f:
            line = json.loads(line)
            text = line['text']
            output = line['output']
            prefix = """This is a named entity recognition task. Refer to the <example> and extract entities from the given <text> based on the <entity labels> provided and follow the <requirements>.

<text>
{}

<entity labels>
<test>,</test>
<Disease>,</Disease>
<treatment>,</treatment>

<example>
Input: The patient is a 38-year-old gentleman, Spanish-speaking, from the Taheimpromong, with no significant past medical history, who presents with shortness of breath x 2 months as well as a dry cough x 1 month.
Output: The patient is a 38-year-old gentleman, Spanish-speaking, from the Taheimpromong, with no significant past medical history, who presents with <Disease>shortness of breath</Disease> x 2 months as well as <Disease>a dry cough</Disease> x 1 month.

Input: In emergency room, he was noted to be afebrile with stable vital signs, was treated with IV fluids, azithromycin, and cefuroxime.
Output: In emergency room, he was noted to be afebrile with stable vital signs, was treated with <treatment>IV fluids</treatment>, <treatment>azithromycin</treatment>, and <treatment>cefuroxime</treatment>.

<requirements>
1. The <entity labels> provided are in the form of <type>,</type>, indicating the start and end tags for the entity type. You need to identify entities within the scope of the given entity types, do not identify entities outside these types.
2. During the identification process, if a continuous segment in the <text> is an entity, it should be marked with the corresponding entity start and end tags.
3. The output format should follow the output format in the <example>."""

            instruction = prefix.format(text)

            data.append({"text": text, "instruction": instruction, "output": output, "task_type": "ner_cluener"})

            if len(instruction) + len(output) > maxlen:
                maxlen = len(instruction) + len(output)
            if len(instruction) > max_source:
                max_source = len(instruction)
            if len(output) > max_target:
                max_target = len(output)

    with open(outputfile, 'w', encoding='utf-8') as f:
        for line in data:
            f.write(json.dumps(line, ensure_ascii=False) + '\n')

    print('maxlen', maxlen)
    print('max_source', max_source)
    print('max_target', max_target)


if __name__ == "__main__":
    inputfile = r'data/AggregationCorpus/SentenceData/i2b2-2010+Llama3-8b生成i2b2-2010_200%/train_processed.json'
    outputfile = r'data/AggregationCorpus/SentenceData/i2b2-2010+Llama3-8b生成i2b2-2010_200%/train_processed_convert_prompt.json'
    convert_ner_cluener_prompt4(inputfile, outputfile)

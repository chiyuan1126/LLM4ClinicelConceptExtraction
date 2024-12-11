import json

file_path = "data/AggregationCorpus/SentenceData/i2b2-2010/train_processed.json"
input_data = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        # 逐行加载 JSON 对象
        json_obj = json.loads(line)
        input_data.append(json_obj)

# 转换为目标格式
output_data = []
for item in input_data:
    # 对 item 单独使用 json.dumps 并应用紧凑的分隔符
    output = item["output"]
    text = item["text"]

    output_item = {
        "instruction": "Please generate named entity recognition data in the biomedical field, with entities including only Disease, test, and treatment. The output should strictly follow this JSON format: {\"text\": \"sentence\",\"outputs\": \"entities in the sentence marked with <type> tags</type>\"}. The example below is only to illustrate the output format, do not generate sentences that are identical or similar to the example. For example: {\"text\": \"On the evening of postoperative day number four, the patient had a transient episode of disorientation and confusion which subsequently resolved spontaneously.\",\"outputs\": \"On the evening of postoperative day number four, the patient had a transient episode of <Disease>disorientation</Disease> and <Disease>confusion</Disease> which subsequently resolved spontaneously.\"}",
        "input": "",
        "output": json.dumps({"text": text, "outputs": output}, ensure_ascii=False)
    }
    # 使用默认的 json.dumps 保持其余部分格式化
    output_data.append(output_item)

# 将结果写入输出文件
with open("data/AggregationCorpus/SentenceData/i2b2-2010/train_processed_generate_apaca.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=2)



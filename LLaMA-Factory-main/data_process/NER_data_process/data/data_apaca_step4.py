import json

file_path = "data/AggregationCorpus/SentenceData/i2b2-2010+Llama3-8b生成i2b2-2010_200%/train_processed_convert_prompt.json"
input_data = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        # 逐行加载 JSON 对象
        json_obj = json.loads(line)
        input_data.append(json_obj)

# 转换为目标格式
output_data = []
for item in input_data:
    output_item = {
        "instruction": item["instruction"],
        "input": "",
        "output": item["output"]
    }
    output_data.append(output_item)

# 将结果写入输出文件
with open("data/AggregationCorpus/SentenceData/i2b2-2010+Llama3-8b生成i2b2-2010_200%/train_processed_convert_apaca.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=2)

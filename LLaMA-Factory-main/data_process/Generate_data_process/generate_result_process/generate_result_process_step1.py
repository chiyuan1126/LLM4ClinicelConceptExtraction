import json

# 读取JSON文件
with open('LLma3-8b/i2b2-2010/new_i2b2_llama3-8b_lora_model_generate10%_train_result_第一步处理.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 创建输出文件
with open('LLma3-8b/i2b2-2010/new_i2b2_llama3-8b_lora_model_generate10%_train_result_第二步处理.tsv', 'w', encoding='utf-8') as f:
    for item in data:
        bio_outputs = item.get('bio_outputs', [])
        for word, tag in bio_outputs:
            f.write(f"{word}\t{tag}\n")
        f.write("\n")  # 每个句子之间用空行隔开

print("BIO格式提取完成，结果已保存到bio_outputs.txt文件中。")

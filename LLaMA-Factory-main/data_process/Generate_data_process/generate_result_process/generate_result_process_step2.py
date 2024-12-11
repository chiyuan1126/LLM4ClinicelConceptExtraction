import json
import re


# 定义一个函数来检查JSON字符串的格式是否正确
def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True
    except ValueError as e:
        return False


# 读取JSON文件
with open(
        'LLma3-8b/i2b2-2010/new_i2b2_llama3-8b_lora_model_generate10%_train_result.json',
        'r', encoding='utf-8') as f:
    data = json.load(f)


def convert_to_bio(text):
    # 定义匹配标签的正则表达式
    pattern = re.compile(r'<(Disease|test|treatment)>(.*?)</\1>')

    # 查找所有匹配的标签和实体
    bio_format = []
    last_index = 0
    cleaned_text = ""

    # 查找所有匹配的标签和实体
    for match in pattern.finditer(text):
        tag = match.group(1)
        entity = match.group(2)
        start, end = match.span(0)

        # 提取标签前的部分文本并添加到清理文本中
        before_entity = text[last_index:start]
        cleaned_text += before_entity
        bio_format.extend([(word, "O") for word in before_entity.split()])

        # 处理实体
        entity_words = entity.split()
        if entity_words:
            bio_format.append((entity_words[0], f"B-{tag}"))
            for word in entity_words[1:]:
                bio_format.append((word, f"I-{tag}"))

        # 添加实体到清理文本中
        cleaned_text += entity
        last_index = end

    # 提取最后一个实体后的部分文本并添加到清理文本中
    after_entity = text[last_index:]
    cleaned_text += after_entity
    bio_format.extend([(word, "O") for word in after_entity.split()])

    return bio_format, cleaned_text


# 遍历数据并转换为BIO格式
for item in data:
    response = item.get('response', None)

    # 打印出当前处理的response
    print(f"Processing response: {response}")

    if response and is_valid_json(response):
        response_dict = json.loads(response)
        text = response_dict.get('outputs', '')
        bio_format, cleaned_text = convert_to_bio(text)
        item['bio_outputs'] = bio_format
        item['cleaned_text'] = cleaned_text
    else:
        print(f"Invalid JSON format in response: {response}")

# 将结果写回到新的JSON文件
with open(
        'LLma3-8b/i2b2-2010/new_i2b2_llama3-8b_lora_model_generate10%_train_result_第一步处理.json',
        'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



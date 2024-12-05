import os
import pandas as pd
import json

# 源目录路径，包含多个文件夹，每个文件夹内有若干txt文件
source_directory = "data/OriginBioData"

# 目标根目录路径，用于保存处理后的文件夹
output_root_directory = "data/AggregationCorpus/SentenceData"

# 确保目标根目录存在
os.makedirs(output_root_directory, exist_ok=True)

# 遍历源目录内的每个文件夹
for folder_name in os.listdir(source_directory):
    folder_path = os.path.join(source_directory, folder_name)

    # 检查是否是文件夹
    if os.path.isdir(folder_path):
        # 创建目标文件夹，与源文件夹名称相同
        output_folder = os.path.join(output_root_directory, folder_name)
        os.makedirs(output_folder, exist_ok=True)

        # 遍历文件夹内的所有txt文件
        for filename in os.listdir(folder_path):
            if filename.endswith(".tsv"):
                # 读取txt文件内容
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "r", encoding="utf-8") as fr:
                    tx = fr.read()

                # 拆分文本并处理数据
                tx = tx.split("\n")
                data = []
                n = 0
                for s in tx:
                    rs = s.split("\t")
                    if len(rs) == 2:
                        data.append([rs[0], rs[1], n])
                    else:
                        n += 1

                # 将数据转换为DataFrame
                data_df = pd.DataFrame(data, columns=["x", "y", "idd"])

                # 输出处理后的数据到JSON文件
                output_filename = os.path.splitext(filename)[0] + "_processed.txt"
                output_path = os.path.join(output_folder, output_filename)

                idds = data_df["idd"].unique().tolist()
                with open(output_path, "a") as fw:
                    for idd in idds:
                        dk = data_df[data_df["idd"] == idd]
                        xx = dk["x"].tolist()
                        yy = dk["y"].tolist()
                        zd = {"id": idd, "text": xx, "labels": yy}
                        zd2 = json.dumps(zd) + "\n"
                        fw.write(zd2)

print('完成')

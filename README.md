> [!NOTE] The model uploading is incomplete since it's too big
# Locally Deplpyed LLM for Clinical Concept Extraction
This is the repository for the experiments codes and models used in "Leveraging Locally Deployed Large Language Models for Clinical Concept Extraction"

## Source Code
All source doe used in this project was uploaded in /LLaMA-Factory-main which was originally forked from https://github.com/hiyouga/LLaMA-Factory

## Prompt Design

## Fine-tuned Models
We evaluated the performance of the following LLMs for acting as a standalone clinical concept extractor.

The LLMs fine-tuned could be download as the following links:
| Models       | Download Link                                      |
| -------------- | --------------------------------------------- |
| Llama3-8b      | [link](https://drive.google.com/drive/folders/1dNAltjNI0-89MYbS_Fvyjm04uI3bDJp2?usp=sharing)     |
| Qwen2-7b       | [link](https://drive.google.com/drive/folders/1oAX47vQOnWPjYNy0SNF7kXN-EHYKTUQ3?usp=sharing)|

Other models are on uploading...

## Results

| Llama3-8b | 0.8821 | 0.8654 | 0.8737 | 0.8023 | 0.7876 | 0.7949 | 0.7945 | 0.6967 | 0.7424 |
| Llama2-7b | 0.8642 | 0.8513 | 0.8577 | 0.7857 | 0.7728 | 0.7792 | 0.7926 | 0.6854 | 0.7351 |
| Qwen2-7b | 0.8776 | 0.8587 | 0.8680 | 0.7946 | 0.7813 | 0.7879 | 0.8141 | 0.702 | 0.7539 |
| Qwen1.5-7b | 0.8747 | 0.8505 | 0.8624 | 0.7936 | 0.78 | 0.7868 | 0.8095 | 0.6962 | 0.7486 |
| Phl3-7b | 0.8818 | 0.8524 | 0.8669 | 0.7906 | 0.786 | 0.7883 | 0.8219 | 0.6827 | 0.7459 |
| Gemma 2-9b | 0.8426 | 0.7653 | 0.8021 | 0.8066 | 0.7974 | 0.802 | 0.8312 | 0.7141 | 0.7682 |
| Mistral-7b | 0.8865 | 0.8727 | 0.8796 | 0.8033 | 0.7939 | 0.7986 | 0.819 | 0.7141 | 0.763 |
| BioClinicalBert+R oBERTa+CRF | 0.8700 | 0.871 | 0.8705 | 0.8000 | 0.7675 | 0.7834 | 0.8079 | 0.8222 | 0.8150 |


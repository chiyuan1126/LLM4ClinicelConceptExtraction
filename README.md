> [!NOTE] The model uploading is incomplete since it's too big
> [!NOTE] Apologize for the typo in the name of the repo. To keep the access link unchanged, we will correct this typo after the manuscript review is completed.
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

## Fine-tuned Models Usage Instructions
When executing the inference command, you need to use the configuration file examples/inference/llama3_lora_sft.yaml to specify the model path, adapter path, template, and other settings. Below are the details of the configuration file.

### Configuration File Parameters：
- `model_name_or_path`：Specifies the path to the original model.
- `adapter_name_or_path`：Specifies the path to the fine-tuned LoRA model.
- `template`：Choose the appropriate template. Different types of models require different templates.
- `finetuning_type`：Specifies the type of fine-tuning.

### Configuration Example：
```yaml
model_name_or_path: meta-llama/Meta-Llama-3-8B-Instruct
adapter_name_or_path: saves/llama3-8b/lora/sft
template: llama3  # Specific model parameters can be found in the LLaMA-Factory project
finetuning_type: lora
```

### After completing the configuration, use the following command for inference：
```bash
llamafactory-cli chat examples/inference/llama3_lora_sft.yaml
```

## Results

### Stand-alone concept extractor

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th colspan="3">i2b2 2010</th>
      <th colspan="3">i2b2 2012</th>
      <th colspan="3">CLEF eHealth Task 2013</th>
    </tr>
    <tr>
      <th></th>
      <th>P</th>
      <th>R</th>
      <th>F-1</th>
      <th>P</th>
      <th>R</th>
      <th>F-1</th>
      <th>P</th>
      <th>R</th>
      <th>F-1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Llama3-8b</td>
      <td>0.8821</td>
      <td>0.8654</td>
      <td>0.8737</td>
      <td>0.8023</td>
      <td>0.7876</td>
      <td>0.7949</td>
      <td>0.7945</td>
      <td>0.6967</td>
      <td>0.7424</td>
    </tr>
    <tr>
      <td>Llama2-7b</td>
      <td>0.8642</td>
      <td>0.8513</td>
      <td>0.8577</td>
      <td>0.7857</td>
      <td>0.7728</td>
      <td>0.7792</td>
      <td>0.7926</td>
      <td>0.6854</td>
      <td>0.7351</td>
    </tr>
    <tr>
      <td>Qwen2-7b</td>
      <td>0.8776</td>
      <td>0.8587</td>
      <td>0.8680</td>
      <td>0.7946</td>
      <td>0.7813</td>
      <td>0.7879</td>
      <td>0.8141</td>
      <td>0.702</td>
      <td>0.7539</td>
    </tr>
    <tr>
      <td>Qwen1.5-7b</td>
      <td>0.8747</td>
      <td>0.8505</td>
      <td>0.8624</td>
      <td>0.7936</td>
      <td>0.78</td>
      <td>0.7868</td>
      <td>0.8095</td>
      <td>0.6962</td>
      <td>0.7486</td>
    </tr>
    <tr>
      <td>Phi3-7b</td>
      <td>0.8818</td>
      <td>0.8524</td>
      <td>0.8669</td>
      <td>0.7906</td>
      <td>0.786</td>
      <td>0.7883</td>
      <td>0.8219</td>
      <td>0.6827</td>
      <td>0.7459</td>
    </tr>
    <tr>
      <td>Gemma 2-9b</td>
      <td>0.8426</td>
      <td>0.7653</td>
      <td>0.8021</td>
      <td>0.8066</td>
      <td>0.7974</td>
      <td>0.802</td>
      <td>0.8312</td>
      <td>0.7141</td>
      <td>0.7682</td>
    </tr>
    <tr>
      <td>Mistral-7b</td>
      <td>0.8865</td>
      <td>0.8727</td>
      <td>0.8796</td>
      <td>0.8033</td>
      <td>0.7939</td>
      <td>0.7986</td>
      <td>0.819</td>
      <td>0.7141</td>
      <td>0.763</td>
    </tr>
    <tr>
      <td>BioClinicalBert+LSTM+CRF</td>
      <td>0.8700</td>
      <td>0.871</td>
      <td>0.8705</td>
      <td>0.8000</td>
      <td>0.7675</td>
      <td>0.7834</td>
      <td>0.8079</td>
      <td>0.8222</td>
      <td>0.8150</td>
    </tr>
  </tbody>
</table>

### Multi-corpus fine-tuned results （i2b2 2010 + i2b2 2012）

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">i2b2 2010</th>
      <th colspan="3">i2b2 2012</th>
    </tr>
    <tr>
      <th></th>
      <th>P</th>
      <th>R</th>
      <th>F-1</th>
      <th>P</th>
      <th>R</th>
      <th>F-1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Llama3-8b</td>
      <td>0.8781</td>
      <td>0.8764</td>
      <td>0.8772</td>
      <td>0.8451</td>
      <td>0.6522</td>
      <td>0.7362</td>
    </tr>
    <tr>
      <td>Qwen2-7b</td>
      <td>0.8755</td>
      <td>0.8722</td>
      <td>0.8738</td>
      <td>0.8455</td>
      <td>0.649</td>
      <td>0.7343</td>
    </tr>
    <tr>
      <td>Gemma 2-9b</td>
      <td>0.8818</td>
      <td>0.7992</td>
      <td>0.8385</td>
      <td>0.8444</td>
      <td>0.655</td>
      <td>0.7377</td>
    </tr>
    <tr>
      <td>Mistral-7b</td>
      <td>0.8832</td>
      <td>0.8814</td>
      <td>0.8823</td>
      <td>0.8445</td>
      <td>0.6547</td>
      <td>0.7376</td>
    </tr>
  </tbody>
</table>

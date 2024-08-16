from huggingface_hub import HfApi
api = HfApi()

api.upload_folder(
    folder_path="D:\\sakana-ai\\sakana-ai-2\\trained_model\\sd-model-finetuned-lora-20240810T122601Z-001\\sd-model-finetuned-lora",
    repo_id="yashvoladoddi37/kanji_to_english_diffusion",
    repo_type="model",
)
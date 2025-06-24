from datasets import load_dataset, load_from_disk
import os


# # Configure paths
datasets_names = ["cais/mmlu", "cais/hle", "Rowan/hellaswag", "TIGER-Lab/MMLU-Pro", "allenai/ai2_arc", "ybisk/piqa", "ehovy/race"]  

save_dir = "D:\\LLM\\Evaluation\\datasets\\mmlu\\"  # Local directory to save

# # Create directory if it doesn't exist
# os.makedirs(save_dir, exist_ok=True)

# # Download and save the dataset
# dataset = load_dataset(dataset_name, 'all')
# dataset.save_to_disk(save_dir)
# print(f"Dataset saved to {save_dir}")


saved_data = load_from_disk(save_dir)
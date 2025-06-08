from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = TFGPT2LMHeadModel.from_pretrained("gpt2")

# GPT-2 has no pad token by default — set it manually
tokenizer.pad_token = tokenizer.eos_token

prompt = input("Enter your prompt: ")

# Now padding will work without crashing
inputs = tokenizer(prompt, return_tensors="tf", padding=True)

outputs = model.generate(
    input_ids=inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    max_length=100,
    do_sample=True,
    temperature=0.8,
    top_p=0.9,
    top_k=50,
    pad_token_id=tokenizer.eos_token_id  # Optional but suppresses another warning
)

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("\nGenerated text:\n", generated_text)

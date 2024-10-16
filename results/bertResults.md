- With the Tokenizer using chunks:
![alt text](image.png)

- With the Tokenizer that truncates to 512 tokens:
![alt text](image-1.png)

- When trying LongForm, we had to reduce the batch sizes, accumulate gradients and use fp16. Still wasn't enough
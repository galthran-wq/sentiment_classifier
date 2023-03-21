# sentiment_classifier

Live demo: http://galthran.pythonanywhere.com/

The model is fine-tuned (only on the labeled data) BERT. </br>
It is available at https://huggingface.co/galthran/distilbert-base-uncased-acllm </br>
Training details are in modeling/test.ipynb. </br>
For logs you can ```% tensorboard --logdir modeling/test_trainer/runs```. </br>
The accuracy for sentiment (binary label) is >90% on the test set, which is SOTA for analagous benchmarks. </br>

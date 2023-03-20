# Can we use ChatGPT for finding fountains in Zurich?
This is a quick hack to explore model fine-tuning of GPT-3 using the OpenAI APIs. Basically it means adding extra layers on top of the LLMs out there. This is a follow-up on my old hack [H2O-Zurich](https://github.com/juntezhang/H2O-Zurich), where instead of using Elasticsearch to query for fountains near me in Zurich, I want to use conversation AI instead. 

It consists of:
- `prepare_data.py` to extract prompt-completion pairs, that can be used to train and build the vector index.
- `app.py`. It creates a GPT vector index on your local machine called index.json which will consist of vector embeddings using text-davinci-003 as the base model. It uses Gradio to create an UI that can be used to ask and get questions.

Previously I have written [a blog post on how question answering](https://github.com/juntezhang/exploring-question-answering) works.

Does it work? Yes it does. After creating the GPT vector index, I started to ask some questions.

I wanted to know if there are any public fountains in Oerlikon, Zurich. Note that Oerlikon is a district within Zurich. And it gives me the correct answer, including the coordinate to the public fountain.
![](images/example1.png)

I also wanted to know if there are any private fountains in Zurich. They may be in courtyards or private property. And yes there are, and it gives me the coordinates to those!
![](images/example2.png)

Finally I get my answer for public fountains in Zurich.
![](images/example3.png)

This would be really powerful when my app can add my geo-coordinates to the question, and shows me the public fountains nearby. I mean, stay hydrated! Especially for free...

### Acknowledgements
This work is supported by **Optimizely**. We unlock digital potential. Optimizely creates digital experiences that transform your company to take data-driven decisions, continued experimentation and constant invention. See https://www.optimizely.com/ and we [are hiring](https://www.optimizely.com/careers/)!
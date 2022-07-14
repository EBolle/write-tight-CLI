# write-tight

This project aims to make you a better business writer with the help of regular expressions. According to a [popular Udemy course on business writing][udemy] we should spend 50% of our writing time on post-writing. In this post-writing phase we make sure our documents are written as clear and concise as possible,
which is sometimes referred to as tight writing.

There are certain <em>patterns</em> in our writing which we want to avoid if we want to write tight. These are patterns that indicate 'deadwood'. According to the [book on tight writing][write-tight] deadwood is the unnecessarily difficult, long, or simply unnecessarily phrases or words that clog the arteries of professional writing. A few examples:

- Words that end on 'ly'
- Passive voice
- Subjunctive mood
- Ambiguous pronouns
- Ambiguous openings

This project detects and color highlights deadwood in your document so you can easily spot and fix them. More information and motivation about improving your business writing with regular expressions can be found in my series of posts on this topic.

- [Improve your writing with regular expressions (part 1)][blogpost-1]
- [Improve your writing with regular expressions (part 2)][blogpost-2]

## Getting started

Currently this project is build to support my personal way of working when I write technical posts for my website. My way of working is writing HTML
directly in VSCode, and rendering the post locally via either a `Flask` server or the `Live Server` extension of VSCode. Since I am already writing
in VSCode I opted to build a CLI since I always have a terminal at my disposal when writing. It's possible that future releases will have a more
user-friendly interface but for now the focus remains on the CLI.

Start by cloning the Github repo and moving in the top directory.

```bash
git clone https://github.com/EBolle/write-tight.git
cd write-tight
```

Next create and activate a new virtual environment and run the following command.

```
pip install -r requirements.txt
```

The write-tight package and its dependencies are now available in your environment.
To use the main functionality of the CLI _first_ open your default browser and then execute the following command
in the terminal.

```bash
wt http://localhost:<your_port>/<your_document>
```

You can also apply the command on live web pages.

```bash
wt https://www.ernst-bolle.com/posts/regex-part-1
```

After running the command your default browser should open a new tab with only the text content of the url
including color highlights for each match of the business writing patterns.

<img src="https://user-images.githubusercontent.com/49920622/179078209-7c466dd9-79b6-4417-9969-594e26468d02.png">

## Limitations

Currently the content of the url needs to adhere to standard HTML guidelines in order to
successfully extract the text from the url. The following HTML elements are extracted:

```bash
['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul']
```

Future releases will likely extend this list or completely change the approach to extract the relevant text.

[udemy]: https://www.udemy.com/course/business-writing-immersion/
[write-tight]: https://www.amazon.nl/Write-Tight-Exactly-Precision-Power/dp/1402210515
[blogpost-1]: https://www.ernst-bolle.com/posts/regex-part-1
[blogpost-2]: https://www.ernst-bolle.com/posts/regex-part-2

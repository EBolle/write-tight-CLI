# write-tight

This project aims to make you a better business writer with the help of regular expressions. According to a [popular Udemy course on business writing][udemy] we should spend 50% of our writing time on post-writing. In this post-writing phase we make sure our documents are written as clear and concise as possible,
which is sometimes referred to as tight writing.

There are certain <em>patterns</em> in our writing which we want to avoid if we want to write tight. These are patterns that indicate 'deadwood'. According to the [book on tight writing][write-tight] deadwood is the unnecessarily difficult, long, or simply unnecessarily phrases or words that clog the arteries of professional writing. A few examples:

- Words that end on 'ly'
- Passive voice
- Subjunctive mood
- Ambiguous pronouns

Besides these patterns good business writing also adheres to a strict structure of your document. Each paragraph should start with a key sentence.
A key sentence needs to be short and clear, and should either be an assertion or a generality. A key sentence summarizes the entire paragraph and
should be enough for someone with little time to get the gist of the paragraph. The summary of your document are all key sentences combined.

If you are looking for information and motivation about improving your business writing with regular expressions please have a look at my series
of posts about this topic.

- [Improve your writing with regular expressions (part 1)][blogpost-1]
- [Improve your writing with regular expressions (part 2)][blogpost-2]

## Getting started

Start by cloning the Github repo and moving in the top directory,

```bash
git clone https://github.com/EBolle/write-tight.git
cd write-tight
```

Next create a new virtual environment and run the following command.

```
pip install -r requirements.txt
```

The dependencies and the write-tight package should now be available in your environment,
and you are ready to use the CLI.

```bash
wt https://<your_url>
```

After running the command your default browser should start with only the text content of the url
including color highlights for each match of the business writing patterns.

## Examples

For most of the development I have used my own blog posts as examples.

```bash
wt https://www.ernst-bolle.com/posts/regex-part-1
```

## Limitations

Currently the content of the url needs to adhere to standard HTML guidelines in order to
successfully extract the text from the url. The following HTML elements are extracted:

```bash
['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul']
```

[udemy]: https://www.udemy.com/course/business-writing-immersion/
[write-tight]: https://www.amazon.nl/Write-Tight-Exactly-Precision-Power/dp/1402210515
[blogpost-1]: https://www.ernst-bolle.com/posts/regex-part-1
[blogpost-2]: https://www.ernst-bolle.com/posts/regex-part-2

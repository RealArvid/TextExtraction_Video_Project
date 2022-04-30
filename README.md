# Text Extraction for Video Project

### Context of this Repository:
This respository is part of a much larger hobby project for my YouTube channel MJ Trial, https://www.youtube.com/channel/UCmcYn20bDrkYlh3V8aIN3vg/, on which I have "recreated" the entire 2005 child molestation trial against Michael Jackson (in total it'll be 200+ hours of video). For some background the trial wasn't televised, so what I have done is that I have taken the orginal court reporter transcripts, formatted the text and added audio using Google Text-to-Speech. Sounds simple? Well, it's been a lot of work to say the least...

### Overall process for Creating Videos:
Videos have been created entirely in Python according to the following four steps (only step 1 is in this repository):
<ol>
  <li>The original court reporter transcripts have reformatted using Regular Expressions.</li>
  <li>Based on the reformatted transcripts, Google Text-to-Speech has been used for speech synthesis. In parallel, Aeneas has been used for synchronizing text and audio.</li>
  <li>Pillow has been used for combining text and speaker pictures into imagery. Approximately, each hour of video consists of roughly 1000 pictures that are created beforehand.</li>
  <li>FFMPEG/MoviePy have been used for putting imagery and audio together into a video.</li>
</ol>

### Description this Repository
This respository corresponds to point 1 above or about 25 % of the total code for the project as a whole. It consists of the following files:
<dl>
  <dt>Formatted Transcripts (folder)</dt>
    <dd>The txt-transcripts contained in this folder is the output from running text_extraction.ipynb</dd>
  
  <dt>Transcripts (folder)
    <dd>This is the original court reporter transcripts and the main input to text_extraction.ipynb</dd>
  
  <dt>changed_speak_names.csv</dt>
    <dd>A CSV file mapping (some of) the speaker names in the original transcipts to the speaker names written to the formatted transcipts. Among other things, it's used to remove unnecessary middle names.</dd>
  
  <dt>read_back_offsets.csv</dt>
    <dd>Of minor importance, this numbers in this file have been manually added so that the correct text is read/displayed when the court reporter reads from the transcripts (e.g. when a question to a witness is reread following an overrruled objection).</dd>
  
  <dt>text_extraction.ipynb</dt>
    <dd>The code doing all the work. It consists of 10 core functions and relies heavily on regular expresssions. At the end of the file there's also some output validation code/functions of less importance.</dd>
</dl>

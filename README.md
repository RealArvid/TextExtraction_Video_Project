# Text Extraction for the Automated Creation of 200+ Hours of Video

This repository contains the text extraction for part of a video project, in which I have "recreated" the entire 2005 child molestation trial against Michael Jackson. Specifically, I have turned all 65 days of court transcripts into over 200 hours of video with text, synchronized audio and an image of the person speaking. To see it for yourself, it is all published on my YouTube channel *MJ Trial*: https://www.youtube.com/channel/UCmcYn20bDrkYlh3V8aIN3vg/.

To put this project in context, the 2005 child molestation trial against Michael Jackson was never televised and no cameras or audio recording equipment were ever allowed in the court room.
<br><br>

### Overview of the Video Creation (this repository corresponds to step 1 ONLY):
Videos have been created entirely in Python and everything has been fully automated. The process can be divided into four steps as follows:
<ol>
  <li>Using Regular Expressions, the text from the 65 court transcripts were extracted and saved into new text files.</li>
  <li>Based on the reformatted transcripts, Google Text-to-Speech was used for speech synthesis. In parallel, the Aeneas library was used to find the timestamps of each word to be able to synchronize text and audio.</li>
  <li>The <i>Pillow</i> library was used to combine text and speaker pictures into imagery. Each hour of video consists of approximately 1000 pictures that were created beforehand.</li>
  <li>FFMPEG/MoviePy was used for putting imagery and audio together into video.</li>
</ol><br>

### Contents of this Respository:
In alphabetical order, this repository contains the following files:

<dl>
  <dt>Formatted Transcripts (folder)</dt>
    <dd>Contains the reformatted text file transcripts, which is the output from text_extraction.ipynb. Compared to the original transcripts, these transcripts are not only much easier for a computer to parse but also much more readable for a human.</dd>
  
  <dt>Transcripts (folder)</dt>
    <dd>Contains the original court transcripts from the trial, which can also be found by a simple Google search. The original court transcripts are the input to text_extraction.ipynb.</dd>
  
  <dt>changed_speak_names.csv</dt>
    <dd>Mapping used to change some (about 25%) of the speaker names in the original transcipts. Mostly it is used to remove middle names.</dd>
  
  <dt>read_back_offsets.csv</dt>
    <dd>Of less importance relative to the other files, the numbers in read_back_offsets.csv have been manually added so that the correct text is read/displayed when the court reporter reads from the transcripts (e.g. when a question to a witness is reread following an overruled objection).</dd>
  
  <dt>text_extraction.ipynb</dt>
    <dd>The Python code for the text extraction. It consists of 10 core functions and makes extensive use of regular expressions. At the end of the file, there are also some not so important code/functions for some relatively limited output validation.</dd>
</dl>

While this repository "only" contains the text extraction part of this project, given how the transcripts are formatted (see Transcripts folder), this has been a major part of the project as whole. Measured by length, text_extraction.ipynb makes up about 1/3 of the code for the project as a whole.
<br><br>

### Final Remarks:
If I were to redo this project, I would definitely make extensive use unit testing to test a variety of inputs to the functions using regular expressions. This would have been extremely helpful as there was almost always some regular expression that had to be added or changed for each of the 65 transcripts. I would also have included a requirements.txt (especially with regards to FFMPEG and Aeneas).

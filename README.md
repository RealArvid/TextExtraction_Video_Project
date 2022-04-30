# TextExtraction

### Context of this Repository:
This respository is part of a much larger hobby project for my YouTube channel MJ Trial, https://www.youtube.com/channel/UCmcYn20bDrkYlh3V8aIN3vg/, on which I have "recreated" the entire 2005 child molestation trial against Michael Jackson (in total it'll be 200+ hours of video). For some background the trial wasn't televised, so what I have done is that I have taken the orginal court reporter transcripts, formatted the texted and added audio using Google Text-to-Speech. Sounds simple? Well, it hasn't been, but I've learnt a lot and really enjoyed the process.

### Overall process for Creating Videos:
Videos have been created entirely in Python according to the following four steps (only step 1 is in this repository):
<ol>
  <li>The original court reporter transcripts have reformatted using Regular Expressions.</li>
  <li>Based on the reformatted transcripts, Google Text-to-Speech has been used for speech synthesis. In parallel, Aeneas has been used for synchronizing text and audio.</li>
  <li>Pillow has been used for combining text and speaker pictures into imagery. Approximately, each hour of video consists of roughly 1000 pictures that are created beforehand.</li>
  <li>FFMPEG/MoviePy have been used for putting imagery and audio together into a video.</li>
</ol>

### Description this Repository
This respository corresponds to point 1 above or about 25 % of the total code for the project as a whole. It consist of the following files:

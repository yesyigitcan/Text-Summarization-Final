

<h2>Contributions</h2>

<ul>
  <li>
    New sentence ranking and word weight calculation methods are added to EdgeSumm technique.
  </li>
  <li>
    Corpus addition on EdgeSumm model.
  </li>
  <li>
    New study on text summarization studies with Turkish language.
  </li>
  <li>
    Text summarization on subjective articles vs objective articles.
  </li>
</ul>

<h2>Differences</h2>

<ul>
  <li>
    ExtendedSumm has an additional part during word weight count. If a word exists in the corpus words list of the corpus which is declared in the document file, this affects positively on its weight value. A constant weight multiplied by word's weight which is calculated in the same manner with EdgeSumm.
  </li>
  <li>
    In ExtendedSumm, positions of the sentences has effect during sentence selection part. Sentence ranks are multiplied by a position value which is calculated during the read of document file. Position weight calculations are done by following an inverse normal distiribution where the sentences in the first and last paragraphs have higher points than sentences close to middle paragraphs of the document and this weight values are between a minimumSentenceWeight set by a user and 1.
  </li>
</ul>

<h2>Observations</h2>

<ul>
  <li>
    ExtendedSumm performs better when document follows the path of description about the topic first and then details but visa-verse when document starts with a warm welcome like 'welcome to my new article' or 'my previous article got 5k likes and thank you all for this'.
  </li>
  <li>
    ExtendedSumm performs better when sentence count of the document increases especially when the sentence count in the same paragraphs under the same subtitle increases.
  </li>
  <li>
    Rogue scores are higher on subjective articles than objective articles. This value might change as dependent on human summaries and other factors. But since objectives articles are more abstract and have less repeated technical words most of the time, these make summarization process harder for autonomous models.
  </li>
</ul>

<h2>Future Work</h2>
  <ul>
    <li>
    Since corpus is used only to check if word exists in corpus but not for complex tasks, an imaginary corpus is created by using the technical words of the sample documents manually. So in the future, corpus creation part should be autonomous.
    </li>
    <li>
    Since studies on Turkish language are not advanced when compared to other languages like English, there might be more failures during parts like pos tagging and stemming. Stanza is used for this study. But more advanced tools may be used or new tool may be created for Turkish language.
    </li>
  </ul>

<h2>Experimental Results</h2>
  
|Document|Sentence Count|Model|Rogue-1|Rogue-2|Rogue-L
|---|---|---|---|---|---|
|Document #3|8|EdgeSumm|0.69565|0.64444|0.69565|
|Document #3|8|ExtendedSumm|0.74434|0.71226|0.74434|
|Document #4|7|EdgeSumm|0.61135|0.50557|0.61135|
|Document #4|7|ExtendedSumm|0.61135|0.50557|0.61135|
|Document #4|8|EdgeSumm|0.56800|0.46465| 0.56800|
|Document #4|8|ExtendedSumm|0.63673|0.54167| 0.63673|
|Document #4|9|EdgeSumm|0.65414|0.53529| 0.65414|
|Document #4|9|ExtendedSumm|0.72031|0.640777|0.72031|
|Document #4|10|EdgeSumm|0.66434|0.58651|0.66434|
|Document #4|10|ExtendedSumm|0.64828|0.56977|0.64828|
|Document #4|12|EdgeSumm|0.68085|0.54867|0.68085|
|Document #4|12|ExtendedSumm|0.60436|0.51414|0.60436|
|Document #5|10|EdgeSumm|0.55801|0.49321|0.55801|
|Document #5|10|ExtendedSumm|0.57224|0.51905|0.57224|
|Document #5|11|EdgeSumm|0.54497|0.42745|0.54497|
|Document #5|11|ExtendedSumm|0.55228|0.48552|0.55228|
|Document #5|12|EdgeSumm|0.56122|0.49057|0.56122|
|Document #5|12|ExtendedSumm|0.57216|0.50107|0.57216|


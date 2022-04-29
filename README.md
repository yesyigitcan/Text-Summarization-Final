|Document|Sentence Count|Model|Rogue-1|Rogue-2|Rogue-L
|--- | ---|---|---|---|---|
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
</ul>

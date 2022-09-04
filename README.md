<h2>Thesis Report</h2>

https://drive.google.com/file/d/1uws1Ji_L2TuCF4Uol-rTQUJZWZr3hn1Y/view?usp=sharing

<h2>Thesis Presentation</h2>

https://docs.google.com/presentation/d/1DAzWLc2SuMQFFmoC9usXSxvOqVRaOV9G61KQC663OYE/edit?usp=sharing

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
    ExtendedSumm performs better when sentence count of the document increases especially when the sentence count in the same paragraphs under the same subtitle increases. In this study, ExtendedSumm showed a poor performance on short sports articles. Because in those articles, each sentence has a possibility of having an important sentece and each sentence is highly informative. So this eliminates the importance of sentence positioning. 
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
  
|Document|Type|Corpus|Sentence Count|Model|Rogue-1 Recall|Rogue-1 Precision|Rogue-1 F1 Score|Rogue-2 Recall|Rogue-2 Precision|Rogue-2 F1 Score|Rogue-L Recall|Rogue-L Precision|Rogue-L F1 Score
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Document #1|Objective|Football|5|EdgeSumm|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|
|Document #1|Objective|Football|5|ExtendedSumm|0.88971|0.7707|0.82594|0.86471|0.76166|0.80992|0.88971|0.7707|0.82594|
|Document #2|Objective|Football|5|EdgeSumm|0.85333|0.84211|0.84768|0.81609|0.85542|0.83529|0.85333|0.84211|0.84768|
|Document #2|Objective|Football|5|ExtendedSumm|0.68|0.70833|0.69388|0.62069|0.66667|0.64286|0.68|0.70833|0.69388|
|Document #2|Objective|Football|6|EdgeSumm|0.86905|0.85882|0.86391|0.84158|0.87629|0.85859|0.86905|0.85882|0.86391|
|Document #2|Objective|Football|6|ExtendedSumm|0.86905|0.85882|0.86391|0.84158|0.87629|0.85859|0.86905|0.85882|0.86391|
|Document #2|Objective|Football|7|EdgeSumm|0.92708|0.92708|0.92708|0.90351|0.9115|0.90749|0.92708|0.92708|0.92708|
|Document #2|Objective|Football|7|ExtendedSumm|0.92708|0.92708|0.92708|0.90351|0.9115|0.90749|0.92708|0.92708|0.92708|
|Document #3|Subjective|Medical|8|EdgeSumm|0.76712|0.63636|0.69565|0.71078|0.58943|0.64444|0.76712|0.63636|0.69565|
|Document #3|Subjective|Medical|8|ExtendedSumm|0.78767|0.70552|0.74434|0.7402|0.68636|0.71226|0.78767|0.70552|0.74434|
|Document #4|Subjective|Psychology|7|EdgeSumm|0.64815|0.57851|0.61135|0.53125|0.48227|0.50558|0.64815|0.57851|0.61135|
|Document #4|Subjective|Psychology|7|ExtendedSumm|0.64815|0.57851|0.61135|0.53125|0.48227|0.50558|0.64815|0.57851|0.61135|
|Document #4|Subjective|Psychology|8|EdgeSumm|0.61207|0.52985|0.568|0.50365|0.43125|0.46465|0.61207|0.52985|0.568|
|Document #4|Subjective|Psychology|8|ExtendedSumm|0.67241|0.60465|0.63673|0.56934|0.51656|0.54167|0.67241|0.60465|0.63673|
|Document #4|Subjective|Psychology|9|EdgeSumm|0.70161|0.61268|0.65414|0.61074|0.53529|0.57053|0.70161|0.61268|0.65414|
|Document #4|Subjective|Psychology|9|ExtendedSumm|0.75806|0.68613|0.72031|0.66443|0.61875|0.64078|0.75806|0.68613|0.72031|
|Document #4|Subjective|Psychology|10|EdgeSumm|0.69853|0.63333|0.66434|0.61728|0.55866|0.58651|0.69853|0.63333|0.66434|
|Document #4|Subjective|Psychology|10|ExtendedSumm|0.69118|0.61039|0.64828|0.60494|0.53846|0.56977|0.69118|0.61039|0.64828|
|Document #4|Subjective|Psychology|12|EdgeSumm|0.76712|0.61202|0.68085|0.69663|0.54867|0.61386|0.76712|0.61202|0.68085|
|Document #4|Subjective|Psychology|12|ExtendedSumm|0.66438|0.55429|0.60436|0.5618|0.47393|0.51414|0.66438|0.55429|0.60436|
|Document #5|Objective|-|10|EdgeSumm|0.61212|0.51269|0.55801|0.55612|0.44309|0.49321|0.61212|0.51269|0.55801|
|Document #5|Objective|-|10|ExtendedSumm|0.61212|0.53723|0.57224|0.55612|0.48661|0.51905|0.61212|0.53723|0.57224|
|Document #5|Objective|-|11|EdgeSumm|0.59538|0.50244|0.54497|0.52913|0.42745|0.47289|0.59538|0.50244|0.54497|
|Document #5|Objective|-|11|ExtendedSumm|0.59538|0.515|0.55228|0.52913|0.44856|0.48552|0.59538|0.515|0.55228|
|Document #5|Objective|-|12|EdgeSumm|0.61111|0.51887|0.56122|0.54419|0.44656|0.49057|0.61111|0.51887|0.56122|
|Document #5|Objective|-|12|ExtendedSumm|0.61667|0.53365|0.57216|0.54419|0.46429|0.50107|0.61667|0.53365|0.57216|


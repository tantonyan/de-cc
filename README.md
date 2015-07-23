## Tigran Antonyan - Coding Challenge

This project is intended for the Insight Data Engineering Coding Challenge.

Here is an overview of the project.

<dl><dt>Language: Python</dt>
<dd>I chose Python for the implementation due to it's popularity within the data engineers and the ease of use. It was very easy to get up to speed with it and I am happy that I've made this choice.</dd></dl>

<dl><dt>Dependencies:</dt> 
<dd>This project depends on the following modules -- all of which seem to be part of the standard Python distribution:
<ul>
 <li>os (and os.path) - get the directory (input) listing and check for the files to work on. </li>
 <li>string - used the string.punctuation constant to "clean-up" the text before processing.</li>
 <li>bisect - maintain a sorted list, this will eliminate the need to sort the list used for the running median problem after each new line is considered, dramatically reducing the run time.</li>
 <li>math - used the floor function to find the "middle index"</li>
</ul>
</dd>
</dl>

<dl><dt>Structure:</dt>
<dd>I followed the suggested structure.<br/>
  &nbsp;<b>/</b> <br/>
  &nbsp;&nbsp;&nbsp;<i>README.md</i><br/>
  &nbsp;&nbsp;&nbsp;<i>run.sh</i> - simple bash script to run the python script, as requested.<br/>
  &nbsp;&nbsp;&nbsp;<b>src/</b><br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>constants.py</i> -- input and output paths<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>helpers.py</i> -- most low level work is done here<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>work.py</i> -- the high level work is done here<br/>
  &nbsp;&nbsp;&nbsp;<b>wc_input/</b></br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>cc_example.txt</i> -- the small example given in the problem description<br/>
  &nbsp;&nbsp;&nbsp;<b>wc_output/</b><br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>med_result.txt</i> -- the output of the running median algorithm for the small example<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>wc_result.txt</i> -- the output of the word count algorithm for the small example<br/>

  *Note:* I added the files to the `wc_input` and `wc_output` directories mainly so that git will add the directories to the repository. I have tested my code against other files as well.
</dd></dl>

<dl><dt>Description of the overall workflow:</dt>
<dd>
 <dl><dt><i>Combined aproach:</i></dt>
  <dd>I have combined the two problems into one process to reduce the operations. Both problems need to open the next available file and read one line at a time (in case the file is too large, it would have been a bad idea to read the entire file into the memory at once) and process it after a "line cleanup" (removing all punctuation characters from it). Thus combining the two problems saves us the second reading process.</dd></dl>

  At first the code (in <i>work.py</i>) gets the list of all items (files and directories) under 
  the input directory, we get this as a list. We sort this list next: the running median
  problem asks us to do so. We then loop through the items and when a file is found we pass
  the path (a relative path to the python scripts - the <i>run.sh</i> first chanages the working dir
  to keep the paths correct) to the top level function of our <i>helpers.py</i> code (`runForFile`),
  which tries to open the file (will skip in case of an error) and if successful, will read
  one line at a time, "clean" it and make a list of words from the resulting string.

  Once we have the words in a list, we pass this to the two separate functions for processing:<br/>
    `addWordsWC` - will process the list of words for the word count problem.<br/>
    `addWordsRM` - will process the same list for the running median problem.

  *Word Count:* We solve this problem by using a global dictionary (`wordCount`) that
              keeps a key:value pairs of already encountered words as word:count. For each
              new line we simply loop through the words and either enter this word with a 
              count of one or increase the count by one if it already exists.

  *Running Median:* We use two global lists for this problem. `wordsPerLine` is a sorted list
                  (we only insert into it using the <i>bisect.insort</i>) of the number of words
                  per line thus far. Once the next number is inserted, our next global list
                  (`runningMedian`) gets appended with the new median.

  When we are done with all of the files we call the two write functions to write out the
  results to the output files. In case of the word count, we first get the list of all keys
  from the global dictionary and sort that list (the order of items in the dictionary is not
  guaranteed and it can not be sorted), we loop through this sorted list, get the count for
  each next word and print out the word/count pair with the requested format. 
  The running median case is easier as we simply need to write out the elements of the 
  `runningMedian` list, one per line.
</dd></dl> 



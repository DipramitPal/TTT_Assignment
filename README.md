   # Terribly Tiny Tales Assignment
# https://assignmentttt.herokuapp.com

**API Calls:**

**POST** to /words

* FORMAT
> { 'count' : 1 }

**RESPONSE**

* FORMAT
> { 'wordName' : 'word','count':45 }

>When a POST Request is made to the Backened in a JSON Format, the request is decrypted and from 'count' argument of the Request, we obtain the limit of the response. In case the limit is not given or negative, we assign it to 0 by default. 

> We split the entire content of the file into words, and after iterating through the list, we obtain the frquency against each word and group them according to each words such that the new array **words_list** has only unique words.

> Now we sort the **words_list** according to the frequency (Since, this is an array of objects) and sort it in descending fashion.

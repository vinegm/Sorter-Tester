<h1>Sorter Tester</h1>

This is a tool for testing sorters in python, and a very simple one at that.

<h2>Used Libraries</h2>

<table>
  <tr>
    <th>Library</th>
    <th>Used For</th>
  </tr>
  <tr>
    <td>numpy</td>
    <td>Array manipulation</td>
  </tr>
  <tr>
    <td>pandas</td>
    <td>Data manipulation</td>
  </tr>
  <tr>
    <td>copy</td>
    <td>Making copies of arrays</td>
  </tr>
  <tr>
   <td>time</td>
   <td>Benchmarking sorting time</td>
  </tr>
  <tr>
   <td>random</td>
   <td>Generating random number</td>
  </tr>
  <tr>
    <td>openpyxl</td>
    <td>Writing dataframes to excel</td>
  </tr>
  <tr>
   <td>matplotlib.pyplot</td>
   <td>Making graphs of the data</td>
  </tr>
  <tr>
   <td>pathlib</td>
   <td>File pathing</td>
  </tr>
</table>

<h2>Selecting Cases</h2>

Opon running the Main.py, it will get the default cases (from 1 to 8) and ask you if you want do add, remove cases, see their description or run them

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/ce43360b-7d31-4a98-9ba0-8db9de26f151)

<h3>description of the built-in cases</h3>

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/e5702783-8083-4b8c-8e2a-bb0402a2eb25)

<h2>Selecting Sorters</h2>

After selecting what cases to run, you will be asked what sorters to run, no one will be selected by default, remember to select at least one of them

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/162239cd-cceb-4130-9dd6-59855364baa6)

<h2>How Many Tests to Run</h2>

Select how many times to benchmark the time the sorter took, so it isn't influenced too much by some system fluke

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/bc2f6fbe-1ca0-4ec2-af5f-5f48c41f727c)

<h2>Testing Phase</h2>

Now it will run the tests, while printing to the console updates when it goes on to test the next sorter or next case

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/8c8e7db6-a354-41a0-8180-8c47d7c8edc8)

<h2>Results</h2>

And at last, it will ask if/how you wish to save the results of the tests

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/b5ec9174-24c8-45c3-82b9-78c6eb9e5ac0)

<h3>Saved Results</h3>

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/9f4c6ded-e69f-475d-9ace-0262b3466e28)

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/c1e20085-c953-4784-8555-782ac02a3dd6)

<h2>Adding Cases/Sorters</h2>

To add a case, you may add it to the testcases.py, adding two dicts, one with the description and one with the actual case, both should have the same key in all lowercases

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/d95e06f5-3cf6-43ec-bd62-bfe386f8bd9c)

And to add a new sorter, add a (sorter name).py in the directory "Sorters", create it and in the __init__.py of the directory add it to the dict of sorters as it follows

![image](https://github.com/vinegm/Sorters-Tester/assets/117782568/822481a7-239f-4769-8d7d-c8e22e8bfe09)

<h2>Thanks for Checking out!</h2>
Thanks for giving a peek at my project, feel free to add test cases and sorters to it as you like, if you find something that I didn't notice feel free to make a pull request to fix it.

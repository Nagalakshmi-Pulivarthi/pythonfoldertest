

```python
import pandas as pd
```


```python
# Create a DataFrame with given columns and value
hey_arnold = pd.DataFrame(
    {"Character_in_show": ["Arnold", "Gerald", "Helga", "Phoebe", "Harold", "Eugene"],
     "color_of_hair": ["blonde", "black","blonde", "black", "unknown", "red"],
     "Height": ["average", "tallish", "tallish", "short", "tall", "short"],
     "Football_Shaped_Head": [True, False, False, False, False, False]
    })

hey_arnold
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Character_in_show</th>
      <th>Football_Shaped_Head</th>
      <th>Height</th>
      <th>color_of_hair</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arnold</td>
      <td>True</td>
      <td>average</td>
      <td>blonde</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gerald</td>
      <td>False</td>
      <td>tallish</td>
      <td>black</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Helga</td>
      <td>False</td>
      <td>tallish</td>
      <td>blonde</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Phoebe</td>
      <td>False</td>
      <td>short</td>
      <td>black</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Harold</td>
      <td>False</td>
      <td>tall</td>
      <td>unknown</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Eugene</td>
      <td>False</td>
      <td>short</td>
      <td>red</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Rename columns for readability
hey_arnold_renamed = hey_arnold.rename(columns={"Character_in_show": "Character",
                                                "color_of_hair": "Hair Color",
                                                "Height": "Height",
                                                "Football_Shaped_Head": "Football Head"
                                               })
hey_arnold_renamed
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Character</th>
      <th>Football Head</th>
      <th>Height</th>
      <th>Hair Color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arnold</td>
      <td>True</td>
      <td>average</td>
      <td>blonde</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gerald</td>
      <td>False</td>
      <td>tallish</td>
      <td>black</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Helga</td>
      <td>False</td>
      <td>tallish</td>
      <td>blonde</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Phoebe</td>
      <td>False</td>
      <td>short</td>
      <td>black</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Harold</td>
      <td>False</td>
      <td>tall</td>
      <td>unknown</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Eugene</td>
      <td>False</td>
      <td>short</td>
      <td>red</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Organize the columns so they are in a more logical order
hey_arnold_alphabetical = hey_arnold_renamed[["Character","Football Head","Hair Color","Height"]]
hey_arnold_alphabetical
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Character</th>
      <th>Football Head</th>
      <th>Hair Color</th>
      <th>Height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arnold</td>
      <td>True</td>
      <td>blonde</td>
      <td>average</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gerald</td>
      <td>False</td>
      <td>black</td>
      <td>tallish</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Helga</td>
      <td>False</td>
      <td>blonde</td>
      <td>tallish</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Phoebe</td>
      <td>False</td>
      <td>black</td>
      <td>short</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Harold</td>
      <td>False</td>
      <td>unknown</td>
      <td>tall</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Eugene</td>
      <td>False</td>
      <td>red</td>
      <td>short</td>
    </tr>
  </tbody>
</table>
</div>




```python
# export new data
hey_arnold_alphabetical.to_csv("output/heyArnold.csv")
```


```python

```

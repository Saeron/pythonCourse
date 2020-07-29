# Import de database


```python
import pandas as pd

df = pd.read_csv("pokemon.cvs")

# print(df.head(3))
```

       #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  \
    0  1  Bulbasaur  Grass  Poison  45      49       49       65       65     45   
    1  2    Ivysaur  Grass  Poison  60      62       63       80       80     60   
    2  3   Venusaur  Grass  Poison  80      82       83      100      100     80   
    
       Generation  Legendary  
    0           1      False  
    1           1      False  
    2           1      False  


# Reding data whit diferet forms


```python
# read columns
df.columns

# read echa column
df[["Name", "Type 1"]]

# read all rows betwen
df.iloc[200:250]

# read a specific location row, column
df.iloc[2,1]

# iterator
# for index, row in df.iterrows():
#     print(index, row["Name"])

# select where
df.loc[df["Type 1"] == "Fire"]

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Charmeleon</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>58</td>
      <td>64</td>
      <td>58</td>
      <td>80</td>
      <td>65</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Charizard</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>78</td>
      <td>84</td>
      <td>78</td>
      <td>109</td>
      <td>85</td>
      <td>100</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6</td>
      <td>CharizardMega Charizard X</td>
      <td>Fire</td>
      <td>Dragon</td>
      <td>78</td>
      <td>130</td>
      <td>111</td>
      <td>130</td>
      <td>85</td>
      <td>100</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>6</td>
      <td>CharizardMega Charizard Y</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>78</td>
      <td>104</td>
      <td>78</td>
      <td>159</td>
      <td>115</td>
      <td>100</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>42</th>
      <td>37</td>
      <td>Vulpix</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>38</td>
      <td>41</td>
      <td>40</td>
      <td>50</td>
      <td>65</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>43</th>
      <td>38</td>
      <td>Ninetales</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>73</td>
      <td>76</td>
      <td>75</td>
      <td>81</td>
      <td>100</td>
      <td>100</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>63</th>
      <td>58</td>
      <td>Growlithe</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>55</td>
      <td>70</td>
      <td>45</td>
      <td>70</td>
      <td>50</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>64</th>
      <td>59</td>
      <td>Arcanine</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>90</td>
      <td>110</td>
      <td>80</td>
      <td>100</td>
      <td>80</td>
      <td>95</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>83</th>
      <td>77</td>
      <td>Ponyta</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>50</td>
      <td>85</td>
      <td>55</td>
      <td>65</td>
      <td>65</td>
      <td>90</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>84</th>
      <td>78</td>
      <td>Rapidash</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>65</td>
      <td>100</td>
      <td>70</td>
      <td>80</td>
      <td>80</td>
      <td>105</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>135</th>
      <td>126</td>
      <td>Magmar</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>65</td>
      <td>95</td>
      <td>57</td>
      <td>100</td>
      <td>85</td>
      <td>93</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>147</th>
      <td>136</td>
      <td>Flareon</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>65</td>
      <td>130</td>
      <td>60</td>
      <td>95</td>
      <td>110</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>158</th>
      <td>146</td>
      <td>Moltres</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>90</td>
      <td>100</td>
      <td>90</td>
      <td>125</td>
      <td>85</td>
      <td>90</td>
      <td>1</td>
      <td>True</td>
    </tr>
    <tr>
      <th>169</th>
      <td>155</td>
      <td>Cyndaquil</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>170</th>
      <td>156</td>
      <td>Quilava</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>58</td>
      <td>64</td>
      <td>58</td>
      <td>80</td>
      <td>65</td>
      <td>80</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>171</th>
      <td>157</td>
      <td>Typhlosion</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>78</td>
      <td>84</td>
      <td>78</td>
      <td>109</td>
      <td>85</td>
      <td>100</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>236</th>
      <td>218</td>
      <td>Slugma</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>40</td>
      <td>40</td>
      <td>40</td>
      <td>70</td>
      <td>40</td>
      <td>20</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>237</th>
      <td>219</td>
      <td>Magcargo</td>
      <td>Fire</td>
      <td>Rock</td>
      <td>50</td>
      <td>50</td>
      <td>120</td>
      <td>80</td>
      <td>80</td>
      <td>30</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>259</th>
      <td>240</td>
      <td>Magby</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>45</td>
      <td>75</td>
      <td>37</td>
      <td>70</td>
      <td>55</td>
      <td>83</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>263</th>
      <td>244</td>
      <td>Entei</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>115</td>
      <td>115</td>
      <td>85</td>
      <td>90</td>
      <td>75</td>
      <td>100</td>
      <td>2</td>
      <td>True</td>
    </tr>
    <tr>
      <th>270</th>
      <td>250</td>
      <td>Ho-oh</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>106</td>
      <td>130</td>
      <td>90</td>
      <td>110</td>
      <td>154</td>
      <td>90</td>
      <td>2</td>
      <td>True</td>
    </tr>
    <tr>
      <th>276</th>
      <td>255</td>
      <td>Torchic</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>45</td>
      <td>60</td>
      <td>40</td>
      <td>70</td>
      <td>50</td>
      <td>45</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>277</th>
      <td>256</td>
      <td>Combusken</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>60</td>
      <td>85</td>
      <td>60</td>
      <td>85</td>
      <td>60</td>
      <td>55</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>278</th>
      <td>257</td>
      <td>Blaziken</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>80</td>
      <td>120</td>
      <td>70</td>
      <td>110</td>
      <td>70</td>
      <td>80</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>279</th>
      <td>257</td>
      <td>BlazikenMega Blaziken</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>80</td>
      <td>160</td>
      <td>80</td>
      <td>130</td>
      <td>80</td>
      <td>100</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>352</th>
      <td>322</td>
      <td>Numel</td>
      <td>Fire</td>
      <td>Ground</td>
      <td>60</td>
      <td>60</td>
      <td>40</td>
      <td>65</td>
      <td>45</td>
      <td>35</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>353</th>
      <td>323</td>
      <td>Camerupt</td>
      <td>Fire</td>
      <td>Ground</td>
      <td>70</td>
      <td>100</td>
      <td>70</td>
      <td>105</td>
      <td>75</td>
      <td>40</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>354</th>
      <td>323</td>
      <td>CameruptMega Camerupt</td>
      <td>Fire</td>
      <td>Ground</td>
      <td>70</td>
      <td>120</td>
      <td>100</td>
      <td>145</td>
      <td>105</td>
      <td>20</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>355</th>
      <td>324</td>
      <td>Torkoal</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>70</td>
      <td>85</td>
      <td>140</td>
      <td>85</td>
      <td>70</td>
      <td>20</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>435</th>
      <td>390</td>
      <td>Chimchar</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>44</td>
      <td>58</td>
      <td>44</td>
      <td>58</td>
      <td>44</td>
      <td>61</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>436</th>
      <td>391</td>
      <td>Monferno</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>64</td>
      <td>78</td>
      <td>52</td>
      <td>78</td>
      <td>52</td>
      <td>81</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>437</th>
      <td>392</td>
      <td>Infernape</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>76</td>
      <td>104</td>
      <td>71</td>
      <td>104</td>
      <td>71</td>
      <td>108</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>518</th>
      <td>467</td>
      <td>Magmortar</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>75</td>
      <td>95</td>
      <td>67</td>
      <td>125</td>
      <td>95</td>
      <td>83</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>542</th>
      <td>485</td>
      <td>Heatran</td>
      <td>Fire</td>
      <td>Steel</td>
      <td>91</td>
      <td>90</td>
      <td>106</td>
      <td>130</td>
      <td>106</td>
      <td>77</td>
      <td>4</td>
      <td>True</td>
    </tr>
    <tr>
      <th>557</th>
      <td>498</td>
      <td>Tepig</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>65</td>
      <td>63</td>
      <td>45</td>
      <td>45</td>
      <td>45</td>
      <td>45</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>558</th>
      <td>499</td>
      <td>Pignite</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>90</td>
      <td>93</td>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>55</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>559</th>
      <td>500</td>
      <td>Emboar</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>110</td>
      <td>123</td>
      <td>65</td>
      <td>100</td>
      <td>65</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>572</th>
      <td>513</td>
      <td>Pansear</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>50</td>
      <td>53</td>
      <td>48</td>
      <td>53</td>
      <td>48</td>
      <td>64</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>573</th>
      <td>514</td>
      <td>Simisear</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>75</td>
      <td>98</td>
      <td>63</td>
      <td>98</td>
      <td>63</td>
      <td>101</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>614</th>
      <td>554</td>
      <td>Darumaka</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>70</td>
      <td>90</td>
      <td>45</td>
      <td>15</td>
      <td>45</td>
      <td>50</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>615</th>
      <td>555</td>
      <td>DarmanitanStandard Mode</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>105</td>
      <td>140</td>
      <td>55</td>
      <td>30</td>
      <td>55</td>
      <td>95</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>616</th>
      <td>555</td>
      <td>DarmanitanZen Mode</td>
      <td>Fire</td>
      <td>Psychic</td>
      <td>105</td>
      <td>30</td>
      <td>105</td>
      <td>140</td>
      <td>105</td>
      <td>55</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>692</th>
      <td>631</td>
      <td>Heatmor</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>85</td>
      <td>97</td>
      <td>66</td>
      <td>105</td>
      <td>66</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>721</th>
      <td>653</td>
      <td>Fennekin</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>40</td>
      <td>45</td>
      <td>40</td>
      <td>62</td>
      <td>60</td>
      <td>60</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>722</th>
      <td>654</td>
      <td>Braixen</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>59</td>
      <td>59</td>
      <td>58</td>
      <td>90</td>
      <td>70</td>
      <td>73</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>723</th>
      <td>655</td>
      <td>Delphox</td>
      <td>Fire</td>
      <td>Psychic</td>
      <td>75</td>
      <td>69</td>
      <td>72</td>
      <td>114</td>
      <td>100</td>
      <td>104</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>730</th>
      <td>662</td>
      <td>Fletchinder</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>62</td>
      <td>73</td>
      <td>55</td>
      <td>56</td>
      <td>52</td>
      <td>84</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>731</th>
      <td>663</td>
      <td>Talonflame</td>
      <td>Fire</td>
      <td>Flying</td>
      <td>78</td>
      <td>81</td>
      <td>71</td>
      <td>74</td>
      <td>69</td>
      <td>126</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>735</th>
      <td>667</td>
      <td>Litleo</td>
      <td>Fire</td>
      <td>Normal</td>
      <td>62</td>
      <td>50</td>
      <td>58</td>
      <td>73</td>
      <td>54</td>
      <td>72</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>736</th>
      <td>668</td>
      <td>Pyroar</td>
      <td>Fire</td>
      <td>Normal</td>
      <td>86</td>
      <td>68</td>
      <td>72</td>
      <td>109</td>
      <td>66</td>
      <td>106</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



# Sorting data


```python
# desviation all stuflick on the code box, and click on the
df.describe()

# sort values
df.sort_values("Name", ascending = True)

# multiple sort values
df.sort_values(["Type 1", "HP"], ascending = [True, False])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>520</th>
      <td>469</td>
      <td>Yanmega</td>
      <td>Bug</td>
      <td>Flying</td>
      <td>86</td>
      <td>76</td>
      <td>86</td>
      <td>116</td>
      <td>56</td>
      <td>95</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>698</th>
      <td>637</td>
      <td>Volcarona</td>
      <td>Bug</td>
      <td>Fire</td>
      <td>85</td>
      <td>60</td>
      <td>65</td>
      <td>135</td>
      <td>105</td>
      <td>100</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>231</th>
      <td>214</td>
      <td>Heracross</td>
      <td>Bug</td>
      <td>Fighting</td>
      <td>80</td>
      <td>125</td>
      <td>75</td>
      <td>40</td>
      <td>95</td>
      <td>85</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>232</th>
      <td>214</td>
      <td>HeracrossMega Heracross</td>
      <td>Bug</td>
      <td>Fighting</td>
      <td>80</td>
      <td>185</td>
      <td>115</td>
      <td>40</td>
      <td>105</td>
      <td>75</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>678</th>
      <td>617</td>
      <td>Accelgor</td>
      <td>Bug</td>
      <td>NaN</td>
      <td>80</td>
      <td>70</td>
      <td>40</td>
      <td>100</td>
      <td>60</td>
      <td>145</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>106</th>
      <td>98</td>
      <td>Krabby</td>
      <td>Water</td>
      <td>NaN</td>
      <td>30</td>
      <td>105</td>
      <td>90</td>
      <td>25</td>
      <td>25</td>
      <td>50</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>125</th>
      <td>116</td>
      <td>Horsea</td>
      <td>Water</td>
      <td>NaN</td>
      <td>30</td>
      <td>40</td>
      <td>70</td>
      <td>70</td>
      <td>25</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>129</th>
      <td>120</td>
      <td>Staryu</td>
      <td>Water</td>
      <td>NaN</td>
      <td>30</td>
      <td>45</td>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>85</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>139</th>
      <td>129</td>
      <td>Magikarp</td>
      <td>Water</td>
      <td>NaN</td>
      <td>20</td>
      <td>10</td>
      <td>55</td>
      <td>15</td>
      <td>20</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>381</th>
      <td>349</td>
      <td>Feebas</td>
      <td>Water</td>
      <td>NaN</td>
      <td>20</td>
      <td>15</td>
      <td>20</td>
      <td>10</td>
      <td>55</td>
      <td>80</td>
      <td>3</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 12 columns</p>
</div>



# Making changes to the data


```python
# creating a new column
# df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]
# df.sort_values("Total", ascending = False)

# drop a column
# df = df.drop(columns = ["Total"])

# another way of do it, axis 1 for horizontal
df["Total"] = df.iloc[:,4:10].sum(axis=1)

# take columns as a list
cols = list(df.columns.values)

# reorganize columns
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# df.head(5)
```

# Saving our Data



```python
# csv file
# df.to_csv("modified.csv", index=False)

# execl file
#df.to_excel("modified.xlsx", index=False)
```

# Filtering Data


```python
# getting only two tipes , 2 wheres, & and, | or
new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")]

# reset index
new_df = df.reset_index(drop=True)

# filltering all contaning a word, negation is whit ~
df.loc[~df["Name"].str.contains("Mega")]

# regular expressions
import re

# re.I ignore capitals, regex=True is needed
df.loc[df["Type 1"].str.contains("fire|grass", flags=re.I, regex=True)]

# all names starting whit pi
df.loc[df["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True)]


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>Legendary</th>
      <th>Total</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20</th>
      <td>16</td>
      <td>Pidgey</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>False</td>
      <td>446</td>
      <td>40</td>
      <td>45</td>
      <td>40</td>
      <td>35</td>
      <td>35</td>
      <td>56</td>
      <td>1</td>
    </tr>
    <tr>
      <th>21</th>
      <td>17</td>
      <td>Pidgeotto</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>False</td>
      <td>627</td>
      <td>63</td>
      <td>60</td>
      <td>55</td>
      <td>50</td>
      <td>50</td>
      <td>71</td>
      <td>1</td>
    </tr>
    <tr>
      <th>22</th>
      <td>18</td>
      <td>Pidgeot</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>False</td>
      <td>857</td>
      <td>83</td>
      <td>80</td>
      <td>75</td>
      <td>70</td>
      <td>70</td>
      <td>101</td>
      <td>1</td>
    </tr>
    <tr>
      <th>23</th>
      <td>18</td>
      <td>PidgeotMega Pidgeot</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>False</td>
      <td>1037</td>
      <td>83</td>
      <td>80</td>
      <td>80</td>
      <td>135</td>
      <td>80</td>
      <td>121</td>
      <td>1</td>
    </tr>
    <tr>
      <th>30</th>
      <td>25</td>
      <td>Pikachu</td>
      <td>Electric</td>
      <td>NaN</td>
      <td>False</td>
      <td>550</td>
      <td>35</td>
      <td>55</td>
      <td>40</td>
      <td>50</td>
      <td>50</td>
      <td>90</td>
      <td>1</td>
    </tr>
    <tr>
      <th>136</th>
      <td>127</td>
      <td>Pinsir</td>
      <td>Bug</td>
      <td>NaN</td>
      <td>False</td>
      <td>915</td>
      <td>65</td>
      <td>125</td>
      <td>100</td>
      <td>55</td>
      <td>70</td>
      <td>85</td>
      <td>1</td>
    </tr>
    <tr>
      <th>137</th>
      <td>127</td>
      <td>PinsirMega Pinsir</td>
      <td>Bug</td>
      <td>Flying</td>
      <td>False</td>
      <td>1095</td>
      <td>65</td>
      <td>155</td>
      <td>120</td>
      <td>65</td>
      <td>90</td>
      <td>105</td>
      <td>1</td>
    </tr>
    <tr>
      <th>186</th>
      <td>172</td>
      <td>Pichu</td>
      <td>Electric</td>
      <td>NaN</td>
      <td>False</td>
      <td>350</td>
      <td>20</td>
      <td>40</td>
      <td>15</td>
      <td>35</td>
      <td>35</td>
      <td>60</td>
      <td>2</td>
    </tr>
    <tr>
      <th>219</th>
      <td>204</td>
      <td>Pineco</td>
      <td>Bug</td>
      <td>NaN</td>
      <td>False</td>
      <td>565</td>
      <td>50</td>
      <td>65</td>
      <td>90</td>
      <td>35</td>
      <td>35</td>
      <td>15</td>
      <td>2</td>
    </tr>
    <tr>
      <th>239</th>
      <td>221</td>
      <td>Piloswine</td>
      <td>Ice</td>
      <td>Ground</td>
      <td>False</td>
      <td>850</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>60</td>
      <td>60</td>
      <td>50</td>
      <td>2</td>
    </tr>
    <tr>
      <th>438</th>
      <td>393</td>
      <td>Piplup</td>
      <td>Water</td>
      <td>NaN</td>
      <td>False</td>
      <td>588</td>
      <td>53</td>
      <td>51</td>
      <td>53</td>
      <td>61</td>
      <td>56</td>
      <td>40</td>
      <td>4</td>
    </tr>
    <tr>
      <th>558</th>
      <td>499</td>
      <td>Pignite</td>
      <td>Fire</td>
      <td>Fighting</td>
      <td>False</td>
      <td>781</td>
      <td>90</td>
      <td>93</td>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>55</td>
      <td>5</td>
    </tr>
    <tr>
      <th>578</th>
      <td>519</td>
      <td>Pidove</td>
      <td>Normal</td>
      <td>Flying</td>
      <td>False</td>
      <td>485</td>
      <td>50</td>
      <td>55</td>
      <td>50</td>
      <td>36</td>
      <td>30</td>
      <td>43</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



# Conditional changes


```python
# changing a parameter
# df.loc[df["Type 1"] == "Flamer", "Type 1"] = "Fire"

#changin multiple parameters
# df.loc[df["Total"] > 500, ["Generation", "Legendary"]] = ["Test1", "Test2"]


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>795</th>
      <td>719</td>
      <td>Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>50</td>
      <td>100</td>
      <td>150</td>
      <td>100</td>
      <td>150</td>
      <td>50</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>796</th>
      <td>719</td>
      <td>DiancieMega Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>50</td>
      <td>160</td>
      <td>110</td>
      <td>160</td>
      <td>110</td>
      <td>110</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>797</th>
      <td>720</td>
      <td>HoopaHoopa Confined</td>
      <td>Psychic</td>
      <td>Ghost</td>
      <td>80</td>
      <td>110</td>
      <td>60</td>
      <td>150</td>
      <td>130</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>798</th>
      <td>720</td>
      <td>HoopaHoopa Unbound</td>
      <td>Psychic</td>
      <td>Dark</td>
      <td>80</td>
      <td>160</td>
      <td>60</td>
      <td>170</td>
      <td>130</td>
      <td>80</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 12 columns</p>
</div>



# Aggregate Statics (Gruopby)


```python
# reloading default csv
df = pd.read_csv("pokemon.cvs")

df.groupby(["Type 1"]).mean().sort_values("Attack", ascending=False)

# you also can use sum() or count()
df.groupby(["Type 1"]).count()["Name"].sort_values(ascending=False)
```




    Type 1
    Water       112
    Normal       98
    Grass        70
    Bug          69
    Psychic      57
    Fire         52
    Rock         44
    Electric     44
    Ground       32
    Dragon       32
    Ghost        32
    Dark         31
    Poison       28
    Steel        27
    Fighting     27
    Ice          24
    Fairy        17
    Flying        4
    Name: Name, dtype: int64



# Working with large amounts of data


```python
# tanking chunks of 5 rows
for df in pd.read_csv("pokemon.cvs", chunksize=5):
    # you can do diferents operations here
    print(df)
```

       #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    0  1              Bulbasaur  Grass  Poison  45      49       49       65   
    1  2                Ivysaur  Grass  Poison  60      62       63       80   
    2  3               Venusaur  Grass  Poison  80      82       83      100   
    3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122   
    4  4             Charmander   Fire     NaN  39      52       43       60   
    
       Sp. Def  Speed  Generation  Legendary  
    0       65     45           1      False  
    1       80     60           1      False  
    2      100     80           1      False  
    3      120     80           1      False  
    4       50     65           1      False  
       #                       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    5  5                 Charmeleon   Fire     NaN  58      64       58       80   
    6  6                  Charizard   Fire  Flying  78      84       78      109   
    7  6  CharizardMega Charizard X   Fire  Dragon  78     130      111      130   
    8  6  CharizardMega Charizard Y   Fire  Flying  78     104       78      159   
    9  7                   Squirtle  Water     NaN  44      48       65       50   
    
       Sp. Def  Speed  Generation  Legendary  
    5       65     80           1      False  
    6       85    100           1      False  
    7       85    100           1      False  
    8      115    100           1      False  
    9       64     43           1      False  
         #                     Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    10   8                Wartortle  Water     NaN  59      63       80       65   
    11   9                Blastoise  Water     NaN  79      83      100       85   
    12   9  BlastoiseMega Blastoise  Water     NaN  79     103      120      135   
    13  10                 Caterpie    Bug     NaN  45      30       35       20   
    14  11                  Metapod    Bug     NaN  50      20       55       25   
    
        Sp. Def  Speed  Generation  Legendary  
    10       80     58           1      False  
    11      105     78           1      False  
    12      115     78           1      False  
    13       20     45           1      False  
    14       25     30           1      False  
         #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    15  12             Butterfree    Bug  Flying  60      45       50       90   
    16  13                 Weedle    Bug  Poison  40      35       30       20   
    17  14                 Kakuna    Bug  Poison  45      25       50       25   
    18  15               Beedrill    Bug  Poison  65      90       40       45   
    19  15  BeedrillMega Beedrill    Bug  Poison  65     150       40       15   
    
        Sp. Def  Speed  Generation  Legendary  
    15       80     70           1      False  
    16       20     50           1      False  
    17       25     35           1      False  
    18       80     75           1      False  
    19       80    145           1      False  
         #                 Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    20  16               Pidgey  Normal  Flying  40      45       40       35   
    21  17            Pidgeotto  Normal  Flying  63      60       55       50   
    22  18              Pidgeot  Normal  Flying  83      80       75       70   
    23  18  PidgeotMega Pidgeot  Normal  Flying  83      80       80      135   
    24  19              Rattata  Normal     NaN  30      56       35       25   
    
        Sp. Def  Speed  Generation  Legendary  
    20       35     56           1      False  
    21       50     71           1      False  
    22       70    101           1      False  
    23       80    121           1      False  
    24       35     72           1      False  
         #      Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    25  20  Raticate  Normal     NaN  55      81       60       50       70   
    26  21   Spearow  Normal  Flying  40      60       30       31       31   
    27  22    Fearow  Normal  Flying  65      90       65       61       61   
    28  23     Ekans  Poison     NaN  35      60       44       40       54   
    29  24     Arbok  Poison     NaN  60      85       69       65       79   
    
        Speed  Generation  Legendary  
    25     97           1      False  
    26     70           1      False  
    27    100           1      False  
    28     55           1      False  
    29     80           1      False  
         #              Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    30  25           Pikachu  Electric     NaN  35      55       40       50   
    31  26            Raichu  Electric     NaN  60      90       55       90   
    32  27         Sandshrew    Ground     NaN  50      75       85       20   
    33  28         Sandslash    Ground     NaN  75     100      110       45   
    34  29  Nidoran (Female)    Poison     NaN  55      47       52       40   
    
        Sp. Def  Speed  Generation  Legendary  
    30       50     90           1      False  
    31       80    110           1      False  
    32       30     40           1      False  
    33       55     65           1      False  
    34       40     41           1      False  
         #            Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    35  30        Nidorina  Poison     NaN  70      62       67       55       55   
    36  31       Nidoqueen  Poison  Ground  90      92       87       75       85   
    37  32  Nidoran (Male)  Poison     NaN  46      57       40       40       40   
    38  33        Nidorino  Poison     NaN  61      72       57       55       55   
    39  34        Nidoking  Poison  Ground  81     102       77       85       75   
    
        Speed  Generation  Legendary  
    35     56           1      False  
    36     76           1      False  
    37     50           1      False  
    38     65           1      False  
    39     85           1      False  
         #        Name  Type 1 Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    40  35    Clefairy   Fairy    NaN   70      45       48       60       65   
    41  36    Clefable   Fairy    NaN   95      70       73       95       90   
    42  37      Vulpix    Fire    NaN   38      41       40       50       65   
    43  38   Ninetales    Fire    NaN   73      76       75       81      100   
    44  39  Jigglypuff  Normal  Fairy  115      45       20       45       25   
    
        Speed  Generation  Legendary  
    40     35           1      False  
    41     60           1      False  
    42     65           1      False  
    43    100           1      False  
    44     20           1      False  
         #        Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    45  40  Wigglytuff  Normal   Fairy  140      70       45       85       50   
    46  41       Zubat  Poison  Flying   40      45       35       30       40   
    47  42      Golbat  Poison  Flying   75      80       70       65       75   
    48  43      Oddish   Grass  Poison   45      50       55       75       65   
    49  44       Gloom   Grass  Poison   60      65       70       85       75   
    
        Speed  Generation  Legendary  
    45     45           1      False  
    46     55           1      False  
    47     90           1      False  
    48     30           1      False  
    49     40           1      False  
         #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    50  45  Vileplume  Grass  Poison  75      80       85      110       90   
    51  46      Paras    Bug   Grass  35      70       55       45       55   
    52  47   Parasect    Bug   Grass  60      95       80       60       80   
    53  48    Venonat    Bug  Poison  60      55       50       40       55   
    54  49   Venomoth    Bug  Poison  70      65       60       90       75   
    
        Speed  Generation  Legendary  
    50     50           1      False  
    51     25           1      False  
    52     30           1      False  
    53     45           1      False  
    54     90           1      False  
         #     Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  \
    55  50  Diglett  Ground     NaN  10      55       25       35       45     95   
    56  51  Dugtrio  Ground     NaN  35      80       50       50       70    120   
    57  52   Meowth  Normal     NaN  40      45       35       40       40     90   
    58  53  Persian  Normal     NaN  65      70       60       65       65    115   
    59  54  Psyduck   Water     NaN  50      52       48       65       50     55   
    
        Generation  Legendary  
    55           1      False  
    56           1      False  
    57           1      False  
    58           1      False  
    59           1      False  
         #       Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    60  55    Golduck     Water     NaN  80      82       78       95       80   
    61  56     Mankey  Fighting     NaN  40      80       35       35       45   
    62  57   Primeape  Fighting     NaN  65     105       60       60       70   
    63  58  Growlithe      Fire     NaN  55      70       45       70       50   
    64  59   Arcanine      Fire     NaN  90     110       80      100       80   
    
        Speed  Generation  Legendary  
    60     85           1      False  
    61     70           1      False  
    62     95           1      False  
    63     60           1      False  
    64     95           1      False  
         #       Name   Type 1    Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    65  60    Poliwag    Water       NaN  40      50       40       40       40   
    66  61  Poliwhirl    Water       NaN  65      65       65       50       50   
    67  62  Poliwrath    Water  Fighting  90      95       95       70       90   
    68  63       Abra  Psychic       NaN  25      20       15      105       55   
    69  64    Kadabra  Psychic       NaN  40      35       30      120       70   
    
        Speed  Generation  Legendary  
    65     90           1      False  
    66     90           1      False  
    67     70           1      False  
    68     90           1      False  
    69    105           1      False  
         #                   Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    70  65               Alakazam   Psychic     NaN  55      50       45      135   
    71  65  AlakazamMega Alakazam   Psychic     NaN  55      50       65      175   
    72  66                 Machop  Fighting     NaN  70      80       50       35   
    73  67                Machoke  Fighting     NaN  80     100       70       50   
    74  68                Machamp  Fighting     NaN  90     130       80       65   
    
        Sp. Def  Speed  Generation  Legendary  
    70       95    120           1      False  
    71       95    150           1      False  
    72       35     35           1      False  
    73       60     45           1      False  
    74       85     55           1      False  
         #        Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    75  69  Bellsprout  Grass  Poison  50      75       35       70       30   
    76  70  Weepinbell  Grass  Poison  65      90       50       85       45   
    77  71  Victreebel  Grass  Poison  80     105       65      100       70   
    78  72   Tentacool  Water  Poison  40      40       35       50      100   
    79  73  Tentacruel  Water  Poison  80      70       65       80      120   
    
        Speed  Generation  Legendary  
    75     40           1      False  
    76     55           1      False  
    77     70           1      False  
    78     70           1      False  
    79    100           1      False  
         #      Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  \
    80  74   Geodude   Rock  Ground  40      80      100       30       30     20   
    81  75  Graveler   Rock  Ground  55      95      115       45       45     35   
    82  76     Golem   Rock  Ground  80     120      130       55       65     45   
    83  77    Ponyta   Fire     NaN  50      85       55       65       65     90   
    84  78  Rapidash   Fire     NaN  65     100       70       80       80    105   
    
        Generation  Legendary  
    80           1      False  
    81           1      False  
    82           1      False  
    83           1      False  
    84           1      False  
         #                 Name    Type 1   Type 2  HP  Attack  Defense  Sp. Atk  \
    85  79             Slowpoke     Water  Psychic  90      65       65       40   
    86  80              Slowbro     Water  Psychic  95      75      110      100   
    87  80  SlowbroMega Slowbro     Water  Psychic  95      75      180      130   
    88  81            Magnemite  Electric    Steel  25      35       70       95   
    89  82             Magneton  Electric    Steel  50      60       95      120   
    
        Sp. Def  Speed  Generation  Legendary  
    85       40     15           1      False  
    86       80     30           1      False  
    87       80     30           1      False  
    88       55     45           1      False  
    89       70     70           1      False  
         #        Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    90  83  Farfetch'd  Normal  Flying  52      65       55       58       62   
    91  84       Doduo  Normal  Flying  35      85       45       35       35   
    92  85      Dodrio  Normal  Flying  60     110       70       60       60   
    93  86        Seel   Water     NaN  65      45       55       45       70   
    94  87     Dewgong   Water     Ice  90      70       80       70       95   
    
        Speed  Generation  Legendary  
    90     60           1      False  
    91     75           1      False  
    92    100           1      False  
    93     45           1      False  
    94     70           1      False  
         #      Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    95  88    Grimer  Poison     NaN   80      80       50       40       50   
    96  89       Muk  Poison     NaN  105     105       75       65      100   
    97  90  Shellder   Water     NaN   30      65      100       45       25   
    98  91  Cloyster   Water     Ice   50      95      180       85       45   
    99  92    Gastly   Ghost  Poison   30      35       30      100       35   
    
        Speed  Generation  Legendary  
    95     25           1      False  
    96     50           1      False  
    97     40           1      False  
    98     70           1      False  
    99     80           1      False  
          #               Name   Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    100  93            Haunter    Ghost  Poison  45      50       45      115   
    101  94             Gengar    Ghost  Poison  60      65       60      130   
    102  94  GengarMega Gengar    Ghost  Poison  60      65       80      170   
    103  95               Onix     Rock  Ground  35      45      160       30   
    104  96            Drowzee  Psychic     NaN  60      48       45       43   
    
         Sp. Def  Speed  Generation  Legendary  
    100       55     95           1      False  
    101       75    110           1      False  
    102       95    130           1      False  
    103       45     70           1      False  
    104       90     42           1      False  
           #       Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    105   97      Hypno   Psychic     NaN  85      73       70       73      115   
    106   98     Krabby     Water     NaN  30     105       90       25       25   
    107   99    Kingler     Water     NaN  55     130      115       50       50   
    108  100    Voltorb  Electric     NaN  40      30       50       55       55   
    109  101  Electrode  Electric     NaN  60      50       70       80       80   
    
         Speed  Generation  Legendary  
    105     67           1      False  
    106     50           1      False  
    107     75           1      False  
    108    100           1      False  
    109    140           1      False  
           #       Name    Type 1   Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    110  102  Exeggcute     Grass  Psychic  60      40       80       60       45   
    111  103  Exeggutor     Grass  Psychic  95      95       85      125       65   
    112  104     Cubone    Ground      NaN  50      50       95       40       50   
    113  105    Marowak    Ground      NaN  60      80      110       50       80   
    114  106  Hitmonlee  Fighting      NaN  50     120       53       35      110   
    
         Speed  Generation  Legendary  
    110     40           1      False  
    111     55           1      False  
    112     35           1      False  
    113     45           1      False  
    114     87           1      False  
           #        Name    Type 1 Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    115  107  Hitmonchan  Fighting    NaN  50     105       79       35      110   
    116  108   Lickitung    Normal    NaN  90      55       75       60       75   
    117  109     Koffing    Poison    NaN  40      65       95       60       45   
    118  110     Weezing    Poison    NaN  65      90      120       85       70   
    119  111     Rhyhorn    Ground   Rock  80      85       95       30       30   
    
         Speed  Generation  Legendary  
    115     76           1      False  
    116     30           1      False  
    117     35           1      False  
    118     60           1      False  
    119     25           1      False  
           #                       Name  Type 1 Type 2   HP  Attack  Defense  \
    120  112                     Rhydon  Ground   Rock  105     130      120   
    121  113                    Chansey  Normal    NaN  250       5        5   
    122  114                    Tangela   Grass    NaN   65      55      115   
    123  115                 Kangaskhan  Normal    NaN  105      95       80   
    124  115  KangaskhanMega Kangaskhan  Normal    NaN  105     125      100   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    120       45       45     40           1      False  
    121       35      105     50           1      False  
    122      100       40     60           1      False  
    123       40       80     90           1      False  
    124       60      100    100           1      False  
           #     Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    125  116   Horsea  Water     NaN  30      40       70       70       25   
    126  117   Seadra  Water     NaN  55      65       95       95       45   
    127  118  Goldeen  Water     NaN  45      67       60       35       50   
    128  119  Seaking  Water     NaN  80      92       65       65       80   
    129  120   Staryu  Water     NaN  30      45       55       70       55   
    
         Speed  Generation  Legendary  
    125     60           1      False  
    126     85           1      False  
    127     63           1      False  
    128     68           1      False  
    129     85           1      False  
           #        Name    Type 1   Type 2  HP  Attack  Defense  Sp. Atk  \
    130  121     Starmie     Water  Psychic  60      75       85      100   
    131  122    Mr. Mime   Psychic    Fairy  40      45       65      100   
    132  123     Scyther       Bug   Flying  70     110       80       55   
    133  124        Jynx       Ice  Psychic  65      50       35      115   
    134  125  Electabuzz  Electric      NaN  65      83       57       95   
    
         Sp. Def  Speed  Generation  Legendary  
    130       85    115           1      False  
    131      120     90           1      False  
    132       80    105           1      False  
    133       95     95           1      False  
    134       85    105           1      False  
           #               Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    135  126             Magmar    Fire     NaN  65      95       57      100   
    136  127             Pinsir     Bug     NaN  65     125      100       55   
    137  127  PinsirMega Pinsir     Bug  Flying  65     155      120       65   
    138  128             Tauros  Normal     NaN  75     100       95       40   
    139  129           Magikarp   Water     NaN  20      10       55       15   
    
         Sp. Def  Speed  Generation  Legendary  
    135       85     93           1      False  
    136       70     85           1      False  
    137       90    105           1      False  
    138       70    110           1      False  
    139       20     80           1      False  
           #                   Name  Type 1  Type 2   HP  Attack  Defense  \
    140  130               Gyarados   Water  Flying   95     125       79   
    141  130  GyaradosMega Gyarados   Water    Dark   95     155      109   
    142  131                 Lapras   Water     Ice  130      85       80   
    143  132                  Ditto  Normal     NaN   48      48       48   
    144  133                  Eevee  Normal     NaN   55      55       50   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    140       60      100     81           1      False  
    141       70      130     81           1      False  
    142       85       95     60           1      False  
    143       48       48     48           1      False  
    144       45       65     55           1      False  
           #      Name    Type 1 Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    145  134  Vaporeon     Water    NaN  130      65       60      110       95   
    146  135   Jolteon  Electric    NaN   65      65       60      110       95   
    147  136   Flareon      Fire    NaN   65     130       60       95      110   
    148  137   Porygon    Normal    NaN   65      60       70       85       75   
    149  138   Omanyte      Rock  Water   35      40      100       90       55   
    
         Speed  Generation  Legendary  
    145     65           1      False  
    146    130           1      False  
    147     65           1      False  
    148     40           1      False  
    149     35           1      False  
           #                       Name Type 1  Type 2  HP  Attack  Defense  \
    150  139                    Omastar   Rock   Water  70      60      125   
    151  140                     Kabuto   Rock   Water  30      80       90   
    152  141                   Kabutops   Rock   Water  60     115      105   
    153  142                 Aerodactyl   Rock  Flying  80     105       65   
    154  142  AerodactylMega Aerodactyl   Rock  Flying  80     135       85   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    150      115       70     55           1      False  
    151       55       45     55           1      False  
    152       65       70     80           1      False  
    153       60       75    130           1      False  
    154       70       95    150           1      False  
           #      Name    Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    155  143   Snorlax    Normal     NaN  160     110       65       65      110   
    156  144  Articuno       Ice  Flying   90      85      100       95      125   
    157  145    Zapdos  Electric  Flying   90      90       85      125       90   
    158  146   Moltres      Fire  Flying   90     100       90      125       85   
    159  147   Dratini    Dragon     NaN   41      64       45       50       50   
    
         Speed  Generation  Legendary  
    155     30           1      False  
    156     85           1       True  
    157    100           1       True  
    158     90           1       True  
    159     50           1      False  
           #                 Name   Type 1    Type 2   HP  Attack  Defense  \
    160  148            Dragonair   Dragon       NaN   61      84       65   
    161  149            Dragonite   Dragon    Flying   91     134       95   
    162  150               Mewtwo  Psychic       NaN  106     110       90   
    163  150  MewtwoMega Mewtwo X  Psychic  Fighting  106     190      100   
    164  150  MewtwoMega Mewtwo Y  Psychic       NaN  106     150       70   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    160       70       70     70           1      False  
    161      100      100     80           1      False  
    162      154       90    130           1       True  
    163      154      100    130           1       True  
    164      194      120    140           1       True  
           #       Name   Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    165  151        Mew  Psychic     NaN  100     100      100      100      100   
    166  152  Chikorita    Grass     NaN   45      49       65       49       65   
    167  153    Bayleef    Grass     NaN   60      62       80       63       80   
    168  154   Meganium    Grass     NaN   80      82      100       83      100   
    169  155  Cyndaquil     Fire     NaN   39      52       43       60       50   
    
         Speed  Generation  Legendary  
    165    100           1      False  
    166     45           2      False  
    167     60           2      False  
    168     80           2      False  
    169     65           2      False  
           #        Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    170  156     Quilava   Fire     NaN  58      64       58       80       65   
    171  157  Typhlosion   Fire     NaN  78      84       78      109       85   
    172  158    Totodile  Water     NaN  50      65       64       44       48   
    173  159    Croconaw  Water     NaN  65      80       80       59       63   
    174  160  Feraligatr  Water     NaN  85     105      100       79       83   
    
         Speed  Generation  Legendary  
    170     80           2      False  
    171    100           2      False  
    172     43           2      False  
    173     58           2      False  
    174     78           2      False  
           #      Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    175  161   Sentret  Normal     NaN   35      46       34       35       45   
    176  162    Furret  Normal     NaN   85      76       64       45       55   
    177  163  Hoothoot  Normal  Flying   60      30       30       36       56   
    178  164   Noctowl  Normal  Flying  100      50       50       76       96   
    179  165    Ledyba     Bug  Flying   40      20       30       40       80   
    
         Speed  Generation  Legendary  
    175     20           2      False  
    176     90           2      False  
    177     50           2      False  
    178     70           2      False  
    179     55           2      False  
           #      Name  Type 1    Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    180  166    Ledian     Bug    Flying  55      35       50       55      110   
    181  167  Spinarak     Bug    Poison  40      60       40       40       40   
    182  168   Ariados     Bug    Poison  70      90       70       60       60   
    183  169    Crobat  Poison    Flying  85      90       80       70       80   
    184  170  Chinchou   Water  Electric  75      38       38       56       56   
    
         Speed  Generation  Legendary  
    180     85           2      False  
    181     30           2      False  
    182     40           2      False  
    183    130           2      False  
    184     67           2      False  
           #       Name    Type 1    Type 2   HP  Attack  Defense  Sp. Atk  \
    185  171    Lanturn     Water  Electric  125      58       58       76   
    186  172      Pichu  Electric       NaN   20      40       15       35   
    187  173     Cleffa     Fairy       NaN   50      25       28       45   
    188  174  Igglybuff    Normal     Fairy   90      30       15       40   
    189  175     Togepi     Fairy       NaN   35      20       65       40   
    
         Sp. Def  Speed  Generation  Legendary  
    185       76     67           2      False  
    186       35     60           2      False  
    187       55     15           2      False  
    188       20     15           2      False  
    189       65     20           2      False  
           #     Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    190  176  Togetic     Fairy  Flying  55      40       85       80      105   
    191  177     Natu   Psychic  Flying  40      50       45       70       45   
    192  178     Xatu   Psychic  Flying  65      75       70       95       70   
    193  179   Mareep  Electric     NaN  55      40       40       65       45   
    194  180  Flaaffy  Electric     NaN  70      55       55       80       60   
    
         Speed  Generation  Legendary  
    190     40           2      False  
    191     70           2      False  
    192     95           2      False  
    193     35           2      False  
    194     45           2      False  
           #                   Name    Type 1  Type 2   HP  Attack  Defense  \
    195  181               Ampharos  Electric     NaN   90      75       85   
    196  181  AmpharosMega Ampharos  Electric  Dragon   90      95      105   
    197  182              Bellossom     Grass     NaN   75      80       95   
    198  183                 Marill     Water   Fairy   70      20       50   
    199  184              Azumarill     Water   Fairy  100      50       80   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    195      115       90     55           2      False  
    196      165      110     45           2      False  
    197       90      100     50           2      False  
    198       20       50     40           2      False  
    199       60       80     50           2      False  
           #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    200  185  Sudowoodo   Rock     NaN  70     100      115       30       65   
    201  186   Politoed  Water     NaN  90      75       75       90      100   
    202  187     Hoppip  Grass  Flying  35      35       40       35       55   
    203  188   Skiploom  Grass  Flying  55      45       50       45       65   
    204  189   Jumpluff  Grass  Flying  75      55       70       55       95   
    
         Speed  Generation  Legendary  
    200     30           2      False  
    201     70           2      False  
    202     50           2      False  
    203     80           2      False  
    204    110           2      False  
           #      Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    205  190     Aipom  Normal     NaN  55      70       55       40       55   
    206  191   Sunkern   Grass     NaN  30      30       30       30       30   
    207  192  Sunflora   Grass     NaN  75      75       55      105       85   
    208  193     Yanma     Bug  Flying  65      65       45       75       45   
    209  194    Wooper   Water  Ground  55      45       45       25       25   
    
         Speed  Generation  Legendary  
    205     85           2      False  
    206     30           2      False  
    207     30           2      False  
    208     95           2      False  
    209     15           2      False  
           #      Name   Type 1   Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    210  195  Quagsire    Water   Ground  95      85       85       65       65   
    211  196    Espeon  Psychic      NaN  65      65       60      130       95   
    212  197   Umbreon     Dark      NaN  95      65      110       60      130   
    213  198   Murkrow     Dark   Flying  60      85       42       85       42   
    214  199  Slowking    Water  Psychic  95      75       80      100      110   
    
         Speed  Generation  Legendary  
    210     35           2      False  
    211    110           2      False  
    212     65           2      False  
    213     91           2      False  
    214     30           2      False  
           #        Name   Type 1   Type 2   HP  Attack  Defense  Sp. Atk  \
    215  200  Misdreavus    Ghost      NaN   60      60       60       85   
    216  201       Unown  Psychic      NaN   48      72       48       72   
    217  202   Wobbuffet  Psychic      NaN  190      33       58       33   
    218  203   Girafarig   Normal  Psychic   70      80       65       90   
    219  204      Pineco      Bug      NaN   50      65       90       35   
    
         Sp. Def  Speed  Generation  Legendary  
    215       85     85           2      False  
    216       48     48           2      False  
    217       58     33           2      False  
    218       65     85           2      False  
    219       35     15           2      False  
           #                 Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  \
    220  205           Forretress     Bug   Steel   75      90      140       60   
    221  206            Dunsparce  Normal     NaN  100      70       70       65   
    222  207               Gligar  Ground  Flying   65      75      105       35   
    223  208              Steelix   Steel  Ground   75      85      200       55   
    224  208  SteelixMega Steelix   Steel  Ground   75     125      230       55   
    
         Sp. Def  Speed  Generation  Legendary  
    220       60     40           2      False  
    221       65     45           2      False  
    222       65     85           2      False  
    223       65     30           2      False  
    224       95     30           2      False  
           #               Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    225  209           Snubbull  Fairy     NaN  60      80       50       40   
    226  210           Granbull  Fairy     NaN  90     120       75       60   
    227  211           Qwilfish  Water  Poison  65      95       75       55   
    228  212             Scizor    Bug   Steel  70     130      100       55   
    229  212  ScizorMega Scizor    Bug   Steel  70     150      140       65   
    
         Sp. Def  Speed  Generation  Legendary  
    225       40     30           2      False  
    226       60     45           2      False  
    227       55     85           2      False  
    228       80     65           2      False  
    229      100     75           2      False  
           #                     Name  Type 1    Type 2  HP  Attack  Defense  \
    230  213                  Shuckle     Bug      Rock  20      10      230   
    231  214                Heracross     Bug  Fighting  80     125       75   
    232  214  HeracrossMega Heracross     Bug  Fighting  80     185      115   
    233  215                  Sneasel    Dark       Ice  55      95       55   
    234  216                Teddiursa  Normal       NaN  60      80       50   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    230       10      230      5           2      False  
    231       40       95     85           2      False  
    232       40      105     75           2      False  
    233       35       75    115           2      False  
    234       50       50     40           2      False  
           #       Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    235  217   Ursaring  Normal     NaN   90     130       75       75       75   
    236  218     Slugma    Fire     NaN   40      40       40       70       40   
    237  219   Magcargo    Fire    Rock   50      50      120       80       80   
    238  220     Swinub     Ice  Ground   50      50       40       30       30   
    239  221  Piloswine     Ice  Ground  100     100       80       60       60   
    
         Speed  Generation  Legendary  
    235     55           2      False  
    236     20           2      False  
    237     30           2      False  
    238     50           2      False  
    239     50           2      False  
           #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    240  222    Corsola  Water    Rock  55      55       85       65       85   
    241  223   Remoraid  Water     NaN  35      65       35       65       35   
    242  224  Octillery  Water     NaN  75     105       75      105       75   
    243  225   Delibird    Ice  Flying  45      55       45       65       45   
    244  226    Mantine  Water  Flying  65      40       70       80      140   
    
         Speed  Generation  Legendary  
    240     35           2      False  
    241     65           2      False  
    242     45           2      False  
    243     75           2      False  
    244     70           2      False  
           #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    245  227               Skarmory  Steel  Flying  65      80      140       40   
    246  228               Houndour   Dark    Fire  45      60       30       80   
    247  229               Houndoom   Dark    Fire  75      90       50      110   
    248  229  HoundoomMega Houndoom   Dark    Fire  75      90       90      140   
    249  230                Kingdra  Water  Dragon  75      95       95       95   
    
         Sp. Def  Speed  Generation  Legendary  
    245       70     70           2      False  
    246       50     65           2      False  
    247       80     95           2      False  
    248       90    115           2      False  
    249       95     85           2      False  
           #      Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    250  231    Phanpy  Ground     NaN  90      60       60       40       40   
    251  232   Donphan  Ground     NaN  90     120      120       60       60   
    252  233  Porygon2  Normal     NaN  85      80       90      105       95   
    253  234  Stantler  Normal     NaN  73      95       62       85       65   
    254  235  Smeargle  Normal     NaN  55      20       35       20       45   
    
         Speed  Generation  Legendary  
    250     40           2      False  
    251     50           2      False  
    252     60           2      False  
    253     85           2      False  
    254     75           2      False  
           #       Name    Type 1   Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    255  236    Tyrogue  Fighting      NaN  35      35       35       35       35   
    256  237  Hitmontop  Fighting      NaN  50      95       95       35      110   
    257  238   Smoochum       Ice  Psychic  45      30       15       85       65   
    258  239     Elekid  Electric      NaN  45      63       37       65       55   
    259  240      Magby      Fire      NaN  45      75       37       70       55   
    
         Speed  Generation  Legendary  
    255     35           2      False  
    256     70           2      False  
    257     65           2      False  
    258     95           2      False  
    259     83           2      False  
           #     Name    Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    260  241  Miltank    Normal     NaN   95      80      105       40       70   
    261  242  Blissey    Normal     NaN  255      10       10       75      135   
    262  243   Raikou  Electric     NaN   90      85       75      115      100   
    263  244    Entei      Fire     NaN  115     115       85       90       75   
    264  245  Suicune     Water     NaN  100      75      115       90      115   
    
         Speed  Generation  Legendary  
    260    100           2      False  
    261     55           2      False  
    262    115           2       True  
    263    100           2       True  
    264     85           2       True  
           #                     Name   Type 1  Type 2   HP  Attack  Defense  \
    265  246                 Larvitar     Rock  Ground   50      64       50   
    266  247                  Pupitar     Rock  Ground   70      84       70   
    267  248                Tyranitar     Rock    Dark  100     134      110   
    268  248  TyranitarMega Tyranitar     Rock    Dark  100     164      150   
    269  249                    Lugia  Psychic  Flying  106      90      130   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    265       45       50     41           2      False  
    266       65       70     51           2      False  
    267       95      100     61           2      False  
    268       95      120     71           2      False  
    269       90      154    110           2       True  
           #      Name   Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    270  250     Ho-oh     Fire  Flying  106     130       90      110      154   
    271  251    Celebi  Psychic   Grass  100     100      100      100      100   
    272  252   Treecko    Grass     NaN   40      45       35       65       55   
    273  253   Grovyle    Grass     NaN   50      65       45       85       65   
    274  254  Sceptile    Grass     NaN   70      85       65      105       85   
    
         Speed  Generation  Legendary  
    270     90           2       True  
    271    100           2      False  
    272     70           3      False  
    273     95           3      False  
    274    120           3      False  
           #                   Name Type 1    Type 2  HP  Attack  Defense  \
    275  254  SceptileMega Sceptile  Grass    Dragon  70     110       75   
    276  255                Torchic   Fire       NaN  45      60       40   
    277  256              Combusken   Fire  Fighting  60      85       60   
    278  257               Blaziken   Fire  Fighting  80     120       70   
    279  257  BlazikenMega Blaziken   Fire  Fighting  80     160       80   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    275      145       85    145           3      False  
    276       70       50     45           3      False  
    277       85       60     55           3      False  
    278      110       70     80           3      False  
    279      130       80    100           3      False  
           #                   Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  \
    280  258                 Mudkip  Water     NaN   50      70       50       50   
    281  259              Marshtomp  Water  Ground   70      85       70       60   
    282  260               Swampert  Water  Ground  100     110       90       85   
    283  260  SwampertMega Swampert  Water  Ground  100     150      110       95   
    284  261              Poochyena   Dark     NaN   35      55       35       30   
    
         Sp. Def  Speed  Generation  Legendary  
    280       50     40           3      False  
    281       70     50           3      False  
    282       90     60           3      False  
    283      110     70           3      False  
    284       30     35           3      False  
           #       Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    285  262  Mightyena    Dark     NaN  70      90       70       60       60   
    286  263  Zigzagoon  Normal     NaN  38      30       41       30       41   
    287  264    Linoone  Normal     NaN  78      70       61       50       61   
    288  265    Wurmple     Bug     NaN  45      45       35       20       30   
    289  266    Silcoon     Bug     NaN  50      35       55       25       25   
    
         Speed  Generation  Legendary  
    285     70           3      False  
    286     60           3      False  
    287    100           3      False  
    288     20           3      False  
    289     15           3      False  
           #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    290  267  Beautifly    Bug  Flying  60      70       50      100       50   
    291  268    Cascoon    Bug     NaN  50      35       55       25       25   
    292  269     Dustox    Bug  Poison  60      50       70       50       90   
    293  270      Lotad  Water   Grass  40      30       30       40       50   
    294  271     Lombre  Water   Grass  60      50       50       60       70   
    
         Speed  Generation  Legendary  
    290     65           3      False  
    291     15           3      False  
    292     65           3      False  
    293     30           3      False  
    294     50           3      False  
           #      Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    295  272  Ludicolo   Water   Grass  80      70       70       90      100   
    296  273    Seedot   Grass     NaN  40      40       50       30       30   
    297  274   Nuzleaf   Grass    Dark  70      70       40       60       40   
    298  275   Shiftry   Grass    Dark  90     100       60       90       60   
    299  276   Taillow  Normal  Flying  40      55       30       30       30   
    
         Speed  Generation  Legendary  
    295     70           3      False  
    296     30           3      False  
    297     60           3      False  
    298     80           3      False  
    299     85           3      False  
           #      Name   Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    300  277   Swellow   Normal  Flying  60      85       60       50       50   
    301  278   Wingull    Water  Flying  40      30       30       55       30   
    302  279  Pelipper    Water  Flying  60      50      100       85       70   
    303  280     Ralts  Psychic   Fairy  28      25       25       45       35   
    304  281    Kirlia  Psychic   Fairy  38      35       35       65       55   
    
         Speed  Generation  Legendary  
    300    125           3      False  
    301     85           3      False  
    302     65           3      False  
    303     40           3      False  
    304     50           3      False  
           #                     Name   Type 1  Type 2  HP  Attack  Defense  \
    305  282                Gardevoir  Psychic   Fairy  68      65       65   
    306  282  GardevoirMega Gardevoir  Psychic   Fairy  68      85       65   
    307  283                  Surskit      Bug   Water  40      30       32   
    308  284               Masquerain      Bug  Flying  70      60       62   
    309  285                Shroomish    Grass     NaN  60      40       60   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    305      125      115     80           3      False  
    306      165      135    100           3      False  
    307       50       52     65           3      False  
    308       80       82     60           3      False  
    309       40       60     35           3      False  
           #      Name  Type 1    Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    310  286   Breloom   Grass  Fighting   60     130       80       60       60   
    311  287   Slakoth  Normal       NaN   60      60       60       35       35   
    312  288  Vigoroth  Normal       NaN   80      80       80       55       55   
    313  289   Slaking  Normal       NaN  150     160      100       95       65   
    314  290   Nincada     Bug    Ground   31      45       90       30       30   
    
         Speed  Generation  Legendary  
    310     70           3      False  
    311     30           3      False  
    312     90           3      False  
    313    100           3      False  
    314     40           3      False  
           #      Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    315  291   Ninjask     Bug  Flying   61      90       45       50       50   
    316  292  Shedinja     Bug   Ghost    1      90       45       30       30   
    317  293   Whismur  Normal     NaN   64      51       23       51       23   
    318  294   Loudred  Normal     NaN   84      71       43       71       43   
    319  295   Exploud  Normal     NaN  104      91       63       91       73   
    
         Speed  Generation  Legendary  
    315    160           3      False  
    316     40           3      False  
    317     28           3      False  
    318     48           3      False  
    319     68           3      False  
           #      Name    Type 1 Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    320  296  Makuhita  Fighting    NaN   72      60       30       20       30   
    321  297  Hariyama  Fighting    NaN  144     120       60       40       60   
    322  298   Azurill    Normal  Fairy   50      20       40       20       40   
    323  299  Nosepass      Rock    NaN   30      45      135       45       90   
    324  300    Skitty    Normal    NaN   50      45       45       35       35   
    
         Speed  Generation  Legendary  
    320     25           3      False  
    321     50           3      False  
    322     20           3      False  
    323     30           3      False  
    324     50           3      False  
           #                 Name  Type 1 Type 2  HP  Attack  Defense  Sp. Atk  \
    325  301             Delcatty  Normal    NaN  70      65       65       55   
    326  302              Sableye    Dark  Ghost  50      75       75       65   
    327  302  SableyeMega Sableye    Dark  Ghost  50      85      125       85   
    328  303               Mawile   Steel  Fairy  50      85       85       55   
    329  303    MawileMega Mawile   Steel  Fairy  50     105      125       55   
    
         Sp. Def  Speed  Generation  Legendary  
    325       55     70           3      False  
    326       65     50           3      False  
    327      115     20           3      False  
    328       55     50           3      False  
    329       95     50           3      False  
           #               Name    Type 1   Type 2  HP  Attack  Defense  Sp. Atk  \
    330  304               Aron     Steel     Rock  50      70      100       40   
    331  305             Lairon     Steel     Rock  60      90      140       50   
    332  306             Aggron     Steel     Rock  70     110      180       60   
    333  306  AggronMega Aggron     Steel      NaN  70     140      230       60   
    334  307           Meditite  Fighting  Psychic  30      40       55       40   
    
         Sp. Def  Speed  Generation  Legendary  
    330       40     30           3      False  
    331       50     40           3      False  
    332       60     50           3      False  
    333       80     50           3      False  
    334       55     60           3      False  
           #                     Name    Type 1   Type 2  HP  Attack  Defense  \
    335  308                 Medicham  Fighting  Psychic  60      60       75   
    336  308    MedichamMega Medicham  Fighting  Psychic  60     100       85   
    337  309                Electrike  Electric      NaN  40      45       40   
    338  310                Manectric  Electric      NaN  70      75       60   
    339  310  ManectricMega Manectric  Electric      NaN  70      75       80   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    335       60       75     80           3      False  
    336       80       85    100           3      False  
    337       65       40     65           3      False  
    338      105       60    105           3      False  
    339      135       80    135           3      False  
           #      Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    340  311    Plusle  Electric     NaN  60      50       40       85       75   
    341  312     Minun  Electric     NaN  60      40       50       75       85   
    342  313   Volbeat       Bug     NaN  65      73       55       47       75   
    343  314  Illumise       Bug     NaN  65      47       55       73       75   
    344  315   Roselia     Grass  Poison  50      60       45      100       80   
    
         Speed  Generation  Legendary  
    340     95           3      False  
    341     95           3      False  
    342     85           3      False  
    343     85           3      False  
    344     65           3      False  
           #                   Name  Type 1 Type 2   HP  Attack  Defense  Sp. Atk  \
    345  316                 Gulpin  Poison    NaN   70      43       53       43   
    346  317                 Swalot  Poison    NaN  100      73       83       73   
    347  318               Carvanha   Water   Dark   45      90       20       65   
    348  319               Sharpedo   Water   Dark   70     120       40       95   
    349  319  SharpedoMega Sharpedo   Water   Dark   70     140       70      110   
    
         Sp. Def  Speed  Generation  Legendary  
    345       53     40           3      False  
    346       83     55           3      False  
    347       20     65           3      False  
    348       40     95           3      False  
    349       65    105           3      False  
           #                   Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  \
    350  320                Wailmer  Water     NaN  130      70       35       70   
    351  321                Wailord  Water     NaN  170      90       45       90   
    352  322                  Numel   Fire  Ground   60      60       40       65   
    353  323               Camerupt   Fire  Ground   70     100       70      105   
    354  323  CameruptMega Camerupt   Fire  Ground   70     120      100      145   
    
         Sp. Def  Speed  Generation  Legendary  
    350       35     60           3      False  
    351       45     60           3      False  
    352       45     35           3      False  
    353       75     40           3      False  
    354      105     20           3      False  
           #      Name   Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    355  324   Torkoal     Fire     NaN  70      85      140       85       70   
    356  325    Spoink  Psychic     NaN  60      25       35       70       80   
    357  326   Grumpig  Psychic     NaN  80      45       65       90      110   
    358  327    Spinda   Normal     NaN  60      60       60       60       60   
    359  328  Trapinch   Ground     NaN  45     100       45       45       45   
    
         Speed  Generation  Legendary  
    355     20           3      False  
    356     60           3      False  
    357     80           3      False  
    358     60           3      False  
    359     10           3      False  
           #      Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    360  329   Vibrava  Ground  Dragon  50      70       50       50       50   
    361  330    Flygon  Ground  Dragon  80     100       80       80       80   
    362  331    Cacnea   Grass     NaN  50      85       40       85       40   
    363  332  Cacturne   Grass    Dark  70     115       60      115       60   
    364  333    Swablu  Normal  Flying  45      40       60       40       75   
    
         Speed  Generation  Legendary  
    360     70           3      False  
    361    100           3      False  
    362     35           3      False  
    363     55           3      False  
    364     50           3      False  
           #                 Name  Type 1   Type 2  HP  Attack  Defense  Sp. Atk  \
    365  334              Altaria  Dragon   Flying  75      70       90       70   
    366  334  AltariaMega Altaria  Dragon    Fairy  75     110      110      110   
    367  335             Zangoose  Normal      NaN  73     115       60       60   
    368  336              Seviper  Poison      NaN  73     100       60      100   
    369  337             Lunatone    Rock  Psychic  70      55       65       95   
    
         Sp. Def  Speed  Generation  Legendary  
    365      105     80           3      False  
    366      105     80           3      False  
    367       60     90           3      False  
    368       60     65           3      False  
    369       85     70           3      False  
           #       Name Type 1   Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    370  338    Solrock   Rock  Psychic   70      95       85       55       65   
    371  339   Barboach  Water   Ground   50      48       43       46       41   
    372  340   Whiscash  Water   Ground  110      78       73       76       71   
    373  341   Corphish  Water      NaN   43      80       65       50       35   
    374  342  Crawdaunt  Water     Dark   63     120       85       90       55   
    
         Speed  Generation  Legendary  
    370     70           3      False  
    371     60           3      False  
    372     60           3      False  
    373     35           3      False  
    374     55           3      False  
           #     Name  Type 1   Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    375  343   Baltoy  Ground  Psychic  40      40       55       40       70   
    376  344  Claydol  Ground  Psychic  60      70      105       70      120   
    377  345   Lileep    Rock    Grass  66      41       77       61       87   
    378  346  Cradily    Rock    Grass  86      81       97       81      107   
    379  347  Anorith    Rock      Bug  45      95       50       40       50   
    
         Speed  Generation  Legendary  
    375     55           3      False  
    376     75           3      False  
    377     23           3      False  
    378     43           3      False  
    379     75           3      False  
           #      Name  Type 1 Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    380  348   Armaldo    Rock    Bug  75     125      100       70       80   
    381  349    Feebas   Water    NaN  20      15       20       10       55   
    382  350   Milotic   Water    NaN  95      60       79      100      125   
    383  351  Castform  Normal    NaN  70      70       70       70       70   
    384  352   Kecleon  Normal    NaN  60      90       70       60      120   
    
         Speed  Generation  Legendary  
    380     45           3      False  
    381     80           3      False  
    382     81           3      False  
    383     70           3      False  
    384     40           3      False  
           #                 Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    385  353              Shuppet  Ghost     NaN  44      75       35       63   
    386  354              Banette  Ghost     NaN  64     115       65       83   
    387  354  BanetteMega Banette  Ghost     NaN  64     165       75       93   
    388  355              Duskull  Ghost     NaN  20      40       90       30   
    389  356             Dusclops  Ghost     NaN  40      70      130       60   
    
         Sp. Def  Speed  Generation  Legendary  
    385       33     45           3      False  
    386       63     65           3      False  
    387       83     75           3      False  
    388       90     25           3      False  
    389      130     25           3      False  
           #             Name   Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    390  357          Tropius    Grass  Flying  99      68       83       72   
    391  358         Chimecho  Psychic     NaN  65      50       70       95   
    392  359            Absol     Dark     NaN  65     130       60       75   
    393  359  AbsolMega Absol     Dark     NaN  65     150       60      115   
    394  360           Wynaut  Psychic     NaN  95      23       48       23   
    
         Sp. Def  Speed  Generation  Legendary  
    390       87     51           3      False  
    391       80     65           3      False  
    392       60     75           3      False  
    393       60    115           3      False  
    394       48     23           3      False  
           #               Name Type 1 Type 2  HP  Attack  Defense  Sp. Atk  \
    395  361            Snorunt    Ice    NaN  50      50       50       50   
    396  362             Glalie    Ice    NaN  80      80       80       80   
    397  362  GlalieMega Glalie    Ice    NaN  80     120       80      120   
    398  363             Spheal    Ice  Water  70      40       50       55   
    399  364             Sealeo    Ice  Water  90      60       70       75   
    
         Sp. Def  Speed  Generation  Legendary  
    395       50     50           3      False  
    396       80     80           3      False  
    397       80    100           3      False  
    398       50     25           3      False  
    399       70     45           3      False  
           #       Name Type 1 Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    400  365    Walrein    Ice  Water  110      80       90       95       90   
    401  366   Clamperl  Water    NaN   35      64       85       74       55   
    402  367    Huntail  Water    NaN   55     104      105       94       75   
    403  368   Gorebyss  Water    NaN   55      84      105      114       75   
    404  369  Relicanth  Water   Rock  100      90      130       45       65   
    
         Speed  Generation  Legendary  
    400     65           3      False  
    401     32           3      False  
    402     52           3      False  
    403     52           3      False  
    404     55           3      False  
           #                     Name  Type 1  Type 2  HP  Attack  Defense  \
    405  370                  Luvdisc   Water     NaN  43      30       55   
    406  371                    Bagon  Dragon     NaN  45      75       60   
    407  372                  Shelgon  Dragon     NaN  65      95      100   
    408  373                Salamence  Dragon  Flying  95     135       80   
    409  373  SalamenceMega Salamence  Dragon  Flying  95     145      130   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    405       40       65     97           3      False  
    406       40       30     50           3      False  
    407       60       50     50           3      False  
    408      110       80    100           3      False  
    409      120       90    120           3      False  
           #                     Name Type 1   Type 2  HP  Attack  Defense  \
    410  374                   Beldum  Steel  Psychic  40      55       80   
    411  375                   Metang  Steel  Psychic  60      75      100   
    412  376                Metagross  Steel  Psychic  80     135      130   
    413  376  MetagrossMega Metagross  Steel  Psychic  80     145      150   
    414  377                 Regirock   Rock      NaN  80     100      200   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    410       35       60     30           3      False  
    411       55       80     50           3      False  
    412       95       90     70           3      False  
    413      105      110    110           3      False  
    414       50      100     50           3       True  
           #               Name  Type 1   Type 2  HP  Attack  Defense  Sp. Atk  \
    415  378             Regice     Ice      NaN  80      50      100      100   
    416  379          Registeel   Steel      NaN  80      75      150       75   
    417  380             Latias  Dragon  Psychic  80      80       90      110   
    418  380  LatiasMega Latias  Dragon  Psychic  80     100      120      140   
    419  381             Latios  Dragon  Psychic  80      90       80      130   
    
         Sp. Def  Speed  Generation  Legendary  
    415      200     50           3       True  
    416      150     50           3       True  
    417      130    110           3       True  
    418      150    110           3       True  
    419      110    110           3       True  
           #                   Name  Type 1   Type 2   HP  Attack  Defense  \
    420  381      LatiosMega Latios  Dragon  Psychic   80     130      100   
    421  382                 Kyogre   Water      NaN  100     100       90   
    422  382    KyogrePrimal Kyogre   Water      NaN  100     150       90   
    423  383                Groudon  Ground      NaN  100     150      140   
    424  383  GroudonPrimal Groudon  Ground     Fire  100     180      160   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    420      160      120    110           3       True  
    421      150      140     90           3       True  
    422      180      160     90           3       True  
    423      100       90     90           3       True  
    424      150       90     90           3       True  
           #                   Name   Type 1   Type 2   HP  Attack  Defense  \
    425  384               Rayquaza   Dragon   Flying  105     150       90   
    426  384  RayquazaMega Rayquaza   Dragon   Flying  105     180      100   
    427  385                Jirachi    Steel  Psychic  100     100      100   
    428  386     DeoxysNormal Forme  Psychic      NaN   50     150       50   
    429  386     DeoxysAttack Forme  Psychic      NaN   50     180       20   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    425      150       90     95           3       True  
    426      180      100    115           3       True  
    427      100      100    100           3       True  
    428      150       50    150           3       True  
    429      180       20    150           3       True  
           #                 Name   Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    430  386  DeoxysDefense Forme  Psychic     NaN  50      70      160       70   
    431  386    DeoxysSpeed Forme  Psychic     NaN  50      95       90       95   
    432  387              Turtwig    Grass     NaN  55      68       64       45   
    433  388               Grotle    Grass     NaN  75      89       85       55   
    434  389             Torterra    Grass  Ground  95     109      105       75   
    
         Sp. Def  Speed  Generation  Legendary  
    430      160     90           3       True  
    431       90    180           3       True  
    432       55     31           4      False  
    433       65     36           4      False  
    434       85     56           4      False  
           #       Name Type 1    Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    435  390   Chimchar   Fire       NaN  44      58       44       58       44   
    436  391   Monferno   Fire  Fighting  64      78       52       78       52   
    437  392  Infernape   Fire  Fighting  76     104       71      104       71   
    438  393     Piplup  Water       NaN  53      51       53       61       56   
    439  394   Prinplup  Water       NaN  64      66       68       81       76   
    
         Speed  Generation  Legendary  
    435     61           4      False  
    436     81           4      False  
    437    108           4      False  
    438     40           4      False  
    439     50           4      False  
           #       Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    440  395   Empoleon   Water   Steel  84      86       88      111      101   
    441  396     Starly  Normal  Flying  40      55       30       30       30   
    442  397   Staravia  Normal  Flying  55      75       50       40       40   
    443  398  Staraptor  Normal  Flying  85     120       70       50       60   
    444  399     Bidoof  Normal     NaN  59      45       40       35       40   
    
         Speed  Generation  Legendary  
    440     60           4      False  
    441     60           4      False  
    442     80           4      False  
    443    100           4      False  
    444     31           4      False  
           #        Name    Type 1 Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    445  400     Bibarel    Normal  Water  79      85       60       55       60   
    446  401   Kricketot       Bug    NaN  37      25       41       25       41   
    447  402  Kricketune       Bug    NaN  77      85       51       55       51   
    448  403       Shinx  Electric    NaN  45      65       34       40       34   
    449  404       Luxio  Electric    NaN  60      85       49       60       49   
    
         Speed  Generation  Legendary  
    445     71           4      False  
    446     25           4      False  
    447     65           4      False  
    448     45           4      False  
    449     60           4      False  
           #       Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    450  405     Luxray  Electric     NaN  80     120       79       95       79   
    451  406      Budew     Grass  Poison  40      30       35       50       70   
    452  407   Roserade     Grass  Poison  60      70       65      125      105   
    453  408   Cranidos      Rock     NaN  67     125       40       30       30   
    454  409  Rampardos      Rock     NaN  97     165       60       65       50   
    
         Speed  Generation  Legendary  
    450     70           4      False  
    451     55           4      False  
    452     90           4      False  
    453     58           4      False  
    454     58           4      False  
           #                 Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    455  410             Shieldon   Rock   Steel  30      42      118       42   
    456  411            Bastiodon   Rock   Steel  60      52      168       47   
    457  412                Burmy    Bug     NaN  40      29       45       29   
    458  413  WormadamPlant Cloak    Bug   Grass  60      59       85       79   
    459  413  WormadamSandy Cloak    Bug  Ground  60      79      105       59   
    
         Sp. Def  Speed  Generation  Legendary  
    455       88     30           4      False  
    456      138     30           4      False  
    457       45     36           4      False  
    458      105     36           4      False  
    459       85     36           4      False  
           #                 Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    460  413  WormadamTrash Cloak       Bug   Steel  60      69       95       69   
    461  414               Mothim       Bug  Flying  70      94       50       94   
    462  415               Combee       Bug  Flying  30      30       42       30   
    463  416            Vespiquen       Bug  Flying  70      80      102       80   
    464  417            Pachirisu  Electric     NaN  60      45       70       45   
    
         Sp. Def  Speed  Generation  Legendary  
    460       95     36           4      False  
    461       50     66           4      False  
    462       42     70           4      False  
    463      102     40           4      False  
    464       90     95           4      False  
           #      Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    465  418    Buizel  Water     NaN  55      65       35       60       30   
    466  419  Floatzel  Water     NaN  85     105       55       85       50   
    467  420   Cherubi  Grass     NaN  45      35       45       62       53   
    468  421   Cherrim  Grass     NaN  70      60       70       87       78   
    469  422   Shellos  Water     NaN  76      48       48       57       62   
    
         Speed  Generation  Legendary  
    465     85           4      False  
    466    115           4      False  
    467     35           4      False  
    468     85           4      False  
    469     34           4      False  
           #       Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    470  423  Gastrodon   Water  Ground  111      83       68       92       82   
    471  424    Ambipom  Normal     NaN   75     100       66       60       66   
    472  425   Drifloon   Ghost  Flying   90      50       34       60       44   
    473  426   Drifblim   Ghost  Flying  150      80       44       90       54   
    474  427    Buneary  Normal     NaN   55      66       44       44       56   
    
         Speed  Generation  Legendary  
    470     39           4      False  
    471    115           4      False  
    472     70           4      False  
    473     80           4      False  
    474     85           4      False  
           #                 Name  Type 1    Type 2   HP  Attack  Defense  \
    475  428              Lopunny  Normal       NaN   65      76       84   
    476  428  LopunnyMega Lopunny  Normal  Fighting   65     136       94   
    477  429            Mismagius   Ghost       NaN   60      60       60   
    478  430            Honchkrow    Dark    Flying  100     125       52   
    479  431              Glameow  Normal       NaN   49      55       42   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    475       54       96    105           4      False  
    476       54       96    135           4      False  
    477      105      105    105           4      False  
    478      105       52     71           4      False  
    479       42       37     85           4      False  
           #       Name   Type 1   Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    480  432    Purugly   Normal      NaN   71      82       64       64       59   
    481  433  Chingling  Psychic      NaN   45      30       50       65       50   
    482  434     Stunky   Poison     Dark   63      63       47       41       41   
    483  435   Skuntank   Poison     Dark  103      93       67       71       61   
    484  436    Bronzor    Steel  Psychic   57      24       86       24       86   
    
         Speed  Generation  Legendary  
    480    112           4      False  
    481     45           4      False  
    482     74           4      False  
    483     84           4      False  
    484     23           4      False  
           #      Name   Type 1   Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    485  437  Bronzong    Steel  Psychic   67      89      116       79      116   
    486  438    Bonsly     Rock      NaN   50      80       95       10       45   
    487  439  Mime Jr.  Psychic    Fairy   20      25       45       70       90   
    488  440   Happiny   Normal      NaN  100       5        5       15       65   
    489  441    Chatot   Normal   Flying   76      65       45       92       42   
    
         Speed  Generation  Legendary  
    485     33           4      False  
    486     10           4      False  
    487     60           4      False  
    488     30           4      False  
    489     91           4      False  
           #                   Name  Type 1  Type 2   HP  Attack  Defense  \
    490  442              Spiritomb   Ghost    Dark   50      92      108   
    491  443                  Gible  Dragon  Ground   58      70       45   
    492  444                 Gabite  Dragon  Ground   68      90       65   
    493  445               Garchomp  Dragon  Ground  108     130       95   
    494  445  GarchompMega Garchomp  Dragon  Ground  108     170      115   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    490       92      108     35           4      False  
    491       40       45     42           4      False  
    492       50       55     82           4      False  
    493       80       85    102           4      False  
    494      120       95     92           4      False  
           #                 Name    Type 1 Type 2   HP  Attack  Defense  Sp. Atk  \
    495  446             Munchlax    Normal    NaN  135      85       40       40   
    496  447                Riolu  Fighting    NaN   40      70       40       35   
    497  448              Lucario  Fighting  Steel   70     110       70      115   
    498  448  LucarioMega Lucario  Fighting  Steel   70     145       88      140   
    499  449           Hippopotas    Ground    NaN   68      72       78       38   
    
         Sp. Def  Speed  Generation  Legendary  
    495       85      5           4      False  
    496       40     60           4      False  
    497       70     90           4      False  
    498       70    112           4      False  
    499       42     32           4      False  
           #       Name  Type 1    Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    500  450  Hippowdon  Ground       NaN  108     112      118       68       72   
    501  451    Skorupi  Poison       Bug   40      50       90       30       55   
    502  452    Drapion  Poison      Dark   70      90      110       60       75   
    503  453   Croagunk  Poison  Fighting   48      61       40       61       40   
    504  454  Toxicroak  Poison  Fighting   83     106       65       86       65   
    
         Speed  Generation  Legendary  
    500     47           4      False  
    501     65           4      False  
    502     95           4      False  
    503     50           4      False  
    504     85           4      False  
           #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    505  455  Carnivine  Grass     NaN  74     100       72       90       72   
    506  456    Finneon  Water     NaN  49      49       56       49       61   
    507  457   Lumineon  Water     NaN  69      69       76       69       86   
    508  458    Mantyke  Water  Flying  45      20       50       60      120   
    509  459     Snover  Grass     Ice  60      62       50       62       60   
    
         Speed  Generation  Legendary  
    505     46           4      False  
    506     66           4      False  
    507     91           4      False  
    508     50           4      False  
    509     40           4      False  
           #                     Name    Type 1 Type 2   HP  Attack  Defense  \
    510  460                Abomasnow     Grass    Ice   90      92       75   
    511  460  AbomasnowMega Abomasnow     Grass    Ice   90     132      105   
    512  461                  Weavile      Dark    Ice   70     120       65   
    513  462                Magnezone  Electric  Steel   70      70      115   
    514  463               Lickilicky    Normal    NaN  110      85       95   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    510       92       85     60           4      False  
    511      132      105     30           4      False  
    512       45       85    125           4      False  
    513      130       90     60           4      False  
    514       80       95     50           4      False  
           #        Name    Type 1  Type 2   HP  Attack  Defense  Sp. Atk  \
    515  464   Rhyperior    Ground    Rock  115     140      130       55   
    516  465   Tangrowth     Grass     NaN  100     100      125      110   
    517  466  Electivire  Electric     NaN   75     123       67       95   
    518  467   Magmortar      Fire     NaN   75      95       67      125   
    519  468    Togekiss     Fairy  Flying   85      50       95      120   
    
         Sp. Def  Speed  Generation  Legendary  
    515       55     40           4      False  
    516       50     50           4      False  
    517       85     95           4      False  
    518       95     83           4      False  
    519      115     80           4      False  
           #       Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    520  469    Yanmega     Bug  Flying   86      76       86      116       56   
    521  470    Leafeon   Grass     NaN   65     110      130       60       65   
    522  471    Glaceon     Ice     NaN   65      60      110      130       95   
    523  472    Gliscor  Ground  Flying   75      95      125       45       75   
    524  473  Mamoswine     Ice  Ground  110     130       80       70       60   
    
         Speed  Generation  Legendary  
    520     95           4      False  
    521     95           4      False  
    522     65           4      False  
    523     95           4      False  
    524     80           4      False  
           #                 Name   Type 1    Type 2  HP  Attack  Defense  \
    525  474            Porygon-Z   Normal       NaN  85      80       70   
    526  475              Gallade  Psychic  Fighting  68     125       65   
    527  475  GalladeMega Gallade  Psychic  Fighting  68     165       95   
    528  476            Probopass     Rock     Steel  60      55      145   
    529  477             Dusknoir    Ghost       NaN  45     100      135   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    525      135       75     90           4      False  
    526       65      115     80           4      False  
    527       65      115    110           4      False  
    528       75      150     40           4      False  
    529       65      135     45           4      False  
           #              Name    Type 1 Type 2  HP  Attack  Defense  Sp. Atk  \
    530  478          Froslass       Ice  Ghost  70      80       70       80   
    531  479             Rotom  Electric  Ghost  50      50       77       95   
    532  479   RotomHeat Rotom  Electric   Fire  50      65      107      105   
    533  479   RotomWash Rotom  Electric  Water  50      65      107      105   
    534  479  RotomFrost Rotom  Electric    Ice  50      65      107      105   
    
         Sp. Def  Speed  Generation  Legendary  
    530       70    110           4      False  
    531       77     91           4      False  
    532      107     86           4      False  
    533      107     86           4      False  
    534      107     86           4      False  
           #            Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
    535  479  RotomFan Rotom  Electric  Flying  50      65      107      105   
    536  479  RotomMow Rotom  Electric   Grass  50      65      107      105   
    537  480            Uxie   Psychic     NaN  75      75      130       75   
    538  481         Mesprit   Psychic     NaN  80     105      105      105   
    539  482           Azelf   Psychic     NaN  75     125       70      125   
    
         Sp. Def  Speed  Generation  Legendary  
    535      107     86           4      False  
    536      107     86           4      False  
    537      130     95           4       True  
    538      105     80           4       True  
    539       70    115           4       True  
           #                   Name  Type 1  Type 2   HP  Attack  Defense  \
    540  483                 Dialga   Steel  Dragon  100     120      120   
    541  484                 Palkia   Water  Dragon   90     120      100   
    542  485                Heatran    Fire   Steel   91      90      106   
    543  486              Regigigas  Normal     NaN  110     160      110   
    544  487  GiratinaAltered Forme   Ghost  Dragon  150     100      120   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    540      150      100     90           4       True  
    541      150      120    100           4       True  
    542      130      106     77           4       True  
    543       80      110    100           4       True  
    544      100      120     90           4       True  
           #                  Name   Type 1  Type 2   HP  Attack  Defense  \
    545  487  GiratinaOrigin Forme    Ghost  Dragon  150     120      100   
    546  488             Cresselia  Psychic     NaN  120      70      120   
    547  489                Phione    Water     NaN   80      80       80   
    548  490               Manaphy    Water     NaN  100     100      100   
    549  491               Darkrai     Dark     NaN   70      90       90   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    545      120      100     90           4       True  
    546       75      130     85           4      False  
    547       80       80     80           4      False  
    548      100      100    100           4      False  
    549      135       90    125           4       True  
           #               Name   Type 1  Type 2   HP  Attack  Defense  Sp. Atk  \
    550  492  ShayminLand Forme    Grass     NaN  100     100      100      100   
    551  492   ShayminSky Forme    Grass  Flying  100     103       75      120   
    552  493             Arceus   Normal     NaN  120     120      120      120   
    553  494            Victini  Psychic    Fire  100     100      100      100   
    554  495              Snivy    Grass     NaN   45      45       55       45   
    
         Sp. Def  Speed  Generation  Legendary  
    550      100    100           4       True  
    551       75    127           4       True  
    552      120    120           4       True  
    553      100    100           5       True  
    554       55     63           5      False  
           #       Name Type 1    Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    555  496    Servine  Grass       NaN   60      60       75       60       75   
    556  497  Serperior  Grass       NaN   75      75       95       75       95   
    557  498      Tepig   Fire       NaN   65      63       45       45       45   
    558  499    Pignite   Fire  Fighting   90      93       55       70       55   
    559  500     Emboar   Fire  Fighting  110     123       65      100       65   
    
         Speed  Generation  Legendary  
    555     83           5      False  
    556    113           5      False  
    557     45           5      False  
    558     55           5      False  
    559     65           5      False  
           #      Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    560  501  Oshawott   Water     NaN  55      55       45       63       45   
    561  502    Dewott   Water     NaN  75      75       60       83       60   
    562  503  Samurott   Water     NaN  95     100       85      108       70   
    563  504    Patrat  Normal     NaN  45      55       39       35       39   
    564  505   Watchog  Normal     NaN  60      85       69       60       69   
    
         Speed  Generation  Legendary  
    560     45           5      False  
    561     60           5      False  
    562     70           5      False  
    563     42           5      False  
    564     77           5      False  
           #       Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    565  506   Lillipup  Normal     NaN  45      60       45       25       45   
    566  507    Herdier  Normal     NaN  65      80       65       35       65   
    567  508  Stoutland  Normal     NaN  85     110       90       45       90   
    568  509   Purrloin    Dark     NaN  41      50       37       50       37   
    569  510    Liepard    Dark     NaN  64      88       50       88       50   
    
         Speed  Generation  Legendary  
    565     55           5      False  
    566     60           5      False  
    567     80           5      False  
    568     66           5      False  
    569    106           5      False  
           #      Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    570  511   Pansage  Grass     NaN  50      53       48       53       48   
    571  512  Simisage  Grass     NaN  75      98       63       98       63   
    572  513   Pansear   Fire     NaN  50      53       48       53       48   
    573  514  Simisear   Fire     NaN  75      98       63       98       63   
    574  515   Panpour  Water     NaN  50      53       48       53       48   
    
         Speed  Generation  Legendary  
    570     64           5      False  
    571    101           5      False  
    572     64           5      False  
    573    101           5      False  
    574     64           5      False  
           #       Name   Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    575  516   Simipour    Water     NaN   75      98       63       98       63   
    576  517      Munna  Psychic     NaN   76      25       45       67       55   
    577  518   Musharna  Psychic     NaN  116      55       85      107       95   
    578  519     Pidove   Normal  Flying   50      55       50       36       30   
    579  520  Tranquill   Normal  Flying   62      77       62       50       42   
    
         Speed  Generation  Legendary  
    575    101           5      False  
    576     24           5      False  
    577     29           5      False  
    578     43           5      False  
    579     65           5      False  
           #        Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    580  521    Unfezant    Normal  Flying  80     115       80       65       55   
    581  522     Blitzle  Electric     NaN  45      60       32       50       32   
    582  523   Zebstrika  Electric     NaN  75     100       63       80       63   
    583  524  Roggenrola      Rock     NaN  55      75       85       25       25   
    584  525     Boldore      Rock     NaN  70     105      105       50       40   
    
         Speed  Generation  Legendary  
    580     93           5      False  
    581     76           5      False  
    582    116           5      False  
    583     15           5      False  
    584     20           5      False  
           #       Name   Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    585  526   Gigalith     Rock     NaN   85     135      130       60       80   
    586  527     Woobat  Psychic  Flying   55      45       43       55       43   
    587  528    Swoobat  Psychic  Flying   67      57       55       77       55   
    588  529    Drilbur   Ground     NaN   60      85       40       30       45   
    589  530  Excadrill   Ground   Steel  110     135       60       50       65   
    
         Speed  Generation  Legendary  
    585     25           5      False  
    586     72           5      False  
    587    114           5      False  
    588     68           5      False  
    589     88           5      False  
           #               Name    Type 1 Type 2   HP  Attack  Defense  Sp. Atk  \
    590  531             Audino    Normal    NaN  103      60       86       60   
    591  531  AudinoMega Audino    Normal  Fairy  103      60      126       80   
    592  532            Timburr  Fighting    NaN   75      80       55       25   
    593  533            Gurdurr  Fighting    NaN   85     105       85       40   
    594  534         Conkeldurr  Fighting    NaN  105     140       95       55   
    
         Sp. Def  Speed  Generation  Legendary  
    590       86     50           5      False  
    591      126     50           5      False  
    592       35     35           5      False  
    593       50     40           5      False  
    594       65     45           5      False  
           #        Name    Type 1  Type 2   HP  Attack  Defense  Sp. Atk  \
    595  535     Tympole     Water     NaN   50      50       40       50   
    596  536   Palpitoad     Water  Ground   75      65       55       65   
    597  537  Seismitoad     Water  Ground  105      95       75       85   
    598  538       Throh  Fighting     NaN  120     100       85       30   
    599  539        Sawk  Fighting     NaN   75     125       75       30   
    
         Sp. Def  Speed  Generation  Legendary  
    595       40     64           5      False  
    596       55     69           5      False  
    597       75     74           5      False  
    598       85     45           5      False  
    599       75     85           5      False  
           #        Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    600  540    Sewaddle    Bug   Grass  45      53       70       40       60   
    601  541    Swadloon    Bug   Grass  55      63       90       50       80   
    602  542    Leavanny    Bug   Grass  75     103       80       70       80   
    603  543    Venipede    Bug  Poison  30      45       59       30       39   
    604  544  Whirlipede    Bug  Poison  40      55       99       40       79   
    
         Speed  Generation  Legendary  
    600     42           5      False  
    601     42           5      False  
    602     92           5      False  
    603     57           5      False  
    604     47           5      False  
           #        Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    605  545   Scolipede    Bug  Poison  60     100       89       55       69   
    606  546    Cottonee  Grass   Fairy  40      27       60       37       50   
    607  547  Whimsicott  Grass   Fairy  60      67       85       77       75   
    608  548     Petilil  Grass     NaN  45      35       50       70       50   
    609  549   Lilligant  Grass     NaN  70      60       75      110       75   
    
         Speed  Generation  Legendary  
    605    112           5      False  
    606     66           5      False  
    607    116           5      False  
    608     30           5      False  
    609     90           5      False  
           #        Name  Type 1 Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    610  550    Basculin   Water    NaN  70      92       65       80       55   
    611  551     Sandile  Ground   Dark  50      72       35       35       35   
    612  552    Krokorok  Ground   Dark  60      82       45       45       45   
    613  553  Krookodile  Ground   Dark  95     117       80       65       70   
    614  554    Darumaka    Fire    NaN  70      90       45       15       45   
    
         Speed  Generation  Legendary  
    610     98           5      False  
    611     65           5      False  
    612     74           5      False  
    613     92           5      False  
    614     50           5      False  
           #                     Name Type 1   Type 2   HP  Attack  Defense  \
    615  555  DarmanitanStandard Mode   Fire      NaN  105     140       55   
    616  555       DarmanitanZen Mode   Fire  Psychic  105      30      105   
    617  556                 Maractus  Grass      NaN   75      86       67   
    618  557                  Dwebble    Bug     Rock   50      65       85   
    619  558                  Crustle    Bug     Rock   70      95      125   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    615       30       55     95           5      False  
    616      140      105     55           5      False  
    617      106       67     60           5      False  
    618       35       35     55           5      False  
    619       65       75     45           5      False  
           #        Name   Type 1    Type 2  HP  Attack  Defense  Sp. Atk  \
    620  559     Scraggy     Dark  Fighting  50      75       70       35   
    621  560     Scrafty     Dark  Fighting  65      90      115       45   
    622  561    Sigilyph  Psychic    Flying  72      58       80      103   
    623  562      Yamask    Ghost       NaN  38      30       85       55   
    624  563  Cofagrigus    Ghost       NaN  58      50      145       95   
    
         Sp. Def  Speed  Generation  Legendary  
    620       70     48           5      False  
    621      115     58           5      False  
    622       80     97           5      False  
    623       65     30           5      False  
    624      105     30           5      False  
           #        Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    625  564    Tirtouga   Water    Rock  54      78      103       53       45   
    626  565  Carracosta   Water    Rock  74     108      133       83       65   
    627  566      Archen    Rock  Flying  55     112       45       74       45   
    628  567    Archeops    Rock  Flying  75     140       65      112       65   
    629  568    Trubbish  Poison     NaN  50      50       62       40       62   
    
         Speed  Generation  Legendary  
    625     22           5      False  
    626     32           5      False  
    627     70           5      False  
    628    110           5      False  
    629     65           5      False  
           #      Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    630  569  Garbodor  Poison     NaN  80      95       82       60       82   
    631  570     Zorua    Dark     NaN  40      65       40       80       40   
    632  571   Zoroark    Dark     NaN  60     105       60      120       60   
    633  572  Minccino  Normal     NaN  55      50       40       40       40   
    634  573  Cinccino  Normal     NaN  75      95       60       65       60   
    
         Speed  Generation  Legendary  
    630     75           5      False  
    631     65           5      False  
    632    105           5      False  
    633     75           5      False  
    634    115           5      False  
           #        Name   Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    635  574     Gothita  Psychic     NaN  45      30       50       55       65   
    636  575   Gothorita  Psychic     NaN  60      45       70       75       85   
    637  576  Gothitelle  Psychic     NaN  70      55       95       95      110   
    638  577     Solosis  Psychic     NaN  45      30       40      105       50   
    639  578     Duosion  Psychic     NaN  65      40       50      125       60   
    
         Speed  Generation  Legendary  
    635     45           5      False  
    636     55           5      False  
    637     65           5      False  
    638     20           5      False  
    639     30           5      False  
           #       Name   Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    640  579  Reuniclus  Psychic     NaN  110      65       75      125       85   
    641  580   Ducklett    Water  Flying   62      44       50       44       50   
    642  581     Swanna    Water  Flying   75      87       63       87       63   
    643  582  Vanillite      Ice     NaN   36      50       50       65       60   
    644  583  Vanillish      Ice     NaN   51      65       65       80       75   
    
         Speed  Generation  Legendary  
    640     30           5      False  
    641     55           5      False  
    642     98           5      False  
    643     44           5      False  
    644     59           5      False  
           #        Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    645  584   Vanilluxe       Ice     NaN  71      95       85      110       95   
    646  585    Deerling    Normal   Grass  60      60       50       40       50   
    647  586    Sawsbuck    Normal   Grass  80     100       70       60       70   
    648  587      Emolga  Electric  Flying  55      75       60       75       60   
    649  588  Karrablast       Bug     NaN  50      75       45       40       45   
    
         Speed  Generation  Legendary  
    645     79           5      False  
    646     75           5      False  
    647     95           5      False  
    648    103           5      False  
    649     60           5      False  
           #        Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    650  589  Escavalier    Bug   Steel   70     135      105       60      105   
    651  590     Foongus  Grass  Poison   69      55       45       55       55   
    652  591   Amoonguss  Grass  Poison  114      85       70       85       80   
    653  592    Frillish  Water   Ghost   55      40       50       65       85   
    654  593   Jellicent  Water   Ghost  100      60       70       85      105   
    
         Speed  Generation  Legendary  
    650     20           5      False  
    651     15           5      False  
    652     30           5      False  
    653     40           5      False  
    654     60           5      False  
           #        Name Type 1    Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    655  594   Alomomola  Water       NaN  165      75       80       40       45   
    656  595      Joltik    Bug  Electric   50      47       50       57       50   
    657  596  Galvantula    Bug  Electric   70      77       60       97       60   
    658  597   Ferroseed  Grass     Steel   44      50       91       24       86   
    659  598  Ferrothorn  Grass     Steel   74      94      131       54      116   
    
         Speed  Generation  Legendary  
    655     65           5      False  
    656     65           5      False  
    657    108           5      False  
    658     10           5      False  
    659     20           5      False  
           #       Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    660  599      Klink     Steel     NaN  40      55       70       45       60   
    661  600      Klang     Steel     NaN  60      80       95       70       85   
    662  601  Klinklang     Steel     NaN  60     100      115       70       85   
    663  602     Tynamo  Electric     NaN  35      55       40       45       40   
    664  603  Eelektrik  Electric     NaN  65      85       70       75       70   
    
         Speed  Generation  Legendary  
    660     30           5      False  
    661     50           5      False  
    662     90           5      False  
    663     60           5      False  
    664     40           5      False  
           #        Name    Type 1 Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    665  604  Eelektross  Electric    NaN  85     115       80      105       80   
    666  605      Elgyem   Psychic    NaN  55      55       55       85       55   
    667  606    Beheeyem   Psychic    NaN  75      75       75      125       95   
    668  607     Litwick     Ghost   Fire  50      30       55       65       55   
    669  608     Lampent     Ghost   Fire  60      40       60       95       60   
    
         Speed  Generation  Legendary  
    665     50           5      False  
    666     30           5      False  
    667     40           5      False  
    668     20           5      False  
    669     55           5      False  
           #        Name  Type 1 Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    670  609  Chandelure   Ghost   Fire  60      55       90      145       90   
    671  610        Axew  Dragon    NaN  46      87       60       30       40   
    672  611     Fraxure  Dragon    NaN  66     117       70       40       50   
    673  612     Haxorus  Dragon    NaN  76     147       90       60       70   
    674  613     Cubchoo     Ice    NaN  55      70       40       60       40   
    
         Speed  Generation  Legendary  
    670     80           5      False  
    671     57           5      False  
    672     67           5      False  
    673     97           5      False  
    674     40           5      False  
           #       Name  Type 1    Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    675  614    Beartic     Ice       NaN   95     110       80       70       80   
    676  615  Cryogonal     Ice       NaN   70      50       30       95      135   
    677  616    Shelmet     Bug       NaN   50      40       85       40       65   
    678  617   Accelgor     Bug       NaN   80      70       40      100       60   
    679  618   Stunfisk  Ground  Electric  109      66       84       81       99   
    
         Speed  Generation  Legendary  
    675     50           5      False  
    676    105           5      False  
    677     25           5      False  
    678    145           5      False  
    679     32           5      False  
           #       Name    Type 1 Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    680  619    Mienfoo  Fighting    NaN  45      85       50       55       50   
    681  620   Mienshao  Fighting    NaN  65     125       60       95       60   
    682  621  Druddigon    Dragon    NaN  77     120       90       60       90   
    683  622     Golett    Ground  Ghost  59      74       50       35       50   
    684  623     Golurk    Ground  Ghost  89     124       80       55       80   
    
         Speed  Generation  Legendary  
    680     65           5      False  
    681    105           5      False  
    682     48           5      False  
    683     35           5      False  
    684     55           5      False  
           #        Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    685  624    Pawniard    Dark   Steel   45      85       70       40       40   
    686  625     Bisharp    Dark   Steel   65     125      100       60       70   
    687  626  Bouffalant  Normal     NaN   95     110       95       40       95   
    688  627     Rufflet  Normal  Flying   70      83       50       37       50   
    689  628    Braviary  Normal  Flying  100     123       75       57       75   
    
         Speed  Generation  Legendary  
    685     60           5      False  
    686     70           5      False  
    687     55           5      False  
    688     60           5      False  
    689     80           5      False  
           #       Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    690  629    Vullaby   Dark  Flying   70      55       75       45       65   
    691  630  Mandibuzz   Dark  Flying  110      65      105       55       95   
    692  631    Heatmor   Fire     NaN   85      97       66      105       66   
    693  632     Durant    Bug   Steel   58     109      112       48       48   
    694  633      Deino   Dark  Dragon   52      65       50       45       50   
    
         Speed  Generation  Legendary  
    690     60           5      False  
    691     80           5      False  
    692     65           5      False  
    693    109           5      False  
    694     38           5      False  
           #       Name Type 1    Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    695  634   Zweilous   Dark    Dragon  72      85       70       65       70   
    696  635  Hydreigon   Dark    Dragon  92     105       90      125       90   
    697  636   Larvesta    Bug      Fire  55      85       55       50       55   
    698  637  Volcarona    Bug      Fire  85      60       65      135      105   
    699  638   Cobalion  Steel  Fighting  91      90      129       90       72   
    
         Speed  Generation  Legendary  
    695     58           5      False  
    696     98           5      False  
    697     60           5      False  
    698    100           5      False  
    699    108           5       True  
           #                      Name    Type 1    Type 2  HP  Attack  Defense  \
    700  639                 Terrakion      Rock  Fighting  91     129       90   
    701  640                  Virizion     Grass  Fighting  91      90       72   
    702  641   TornadusIncarnate Forme    Flying       NaN  79     115       70   
    703  641     TornadusTherian Forme    Flying       NaN  79     100       80   
    704  642  ThundurusIncarnate Forme  Electric    Flying  79     115       70   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    700       72       90    108           5       True  
    701       90      129    108           5       True  
    702      125       80    111           5       True  
    703      110       90    121           5       True  
    704      125       80    111           5       True  
           #                     Name    Type 1    Type 2   HP  Attack  Defense  \
    705  642   ThundurusTherian Forme  Electric    Flying   79     105       70   
    706  643                 Reshiram    Dragon      Fire  100     120      100   
    707  644                   Zekrom    Dragon  Electric  100     150      120   
    708  645  LandorusIncarnate Forme    Ground    Flying   89     125       90   
    709  645    LandorusTherian Forme    Ground    Flying   89     145       90   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    705      145       80    101           5       True  
    706      150      120     90           5       True  
    707      120      100     90           5       True  
    708      115       80    101           5       True  
    709      105       80     91           5       True  
           #                  Name  Type 1    Type 2   HP  Attack  Defense  \
    710  646                Kyurem  Dragon       Ice  125     130       90   
    711  646    KyuremBlack Kyurem  Dragon       Ice  125     170      100   
    712  646    KyuremWhite Kyurem  Dragon       Ice  125     120       90   
    713  647  KeldeoOrdinary Forme   Water  Fighting   91      72       90   
    714  647  KeldeoResolute Forme   Water  Fighting   91      72       90   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    710      130       90     95           5       True  
    711      120       90     95           5       True  
    712      170      100     95           5       True  
    713      129       90    108           5      False  
    714      129       90    108           5      False  
           #                     Name  Type 1    Type 2   HP  Attack  Defense  \
    715  648       MeloettaAria Forme  Normal   Psychic  100      77       77   
    716  648  MeloettaPirouette Forme  Normal  Fighting  100     128       90   
    717  649                 Genesect     Bug     Steel   71     120       95   
    718  650                  Chespin   Grass       NaN   56      61       65   
    719  651                Quilladin   Grass       NaN   61      78       95   
    
         Sp. Atk  Sp. Def  Speed  Generation  Legendary  
    715      128      128     90           5      False  
    716       77       77    128           5      False  
    717      120       95     99           5      False  
    718       48       45     38           6      False  
    719       56       58     57           6      False  
           #        Name Type 1    Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    720  652  Chesnaught  Grass  Fighting  88     107      122       74       75   
    721  653    Fennekin   Fire       NaN  40      45       40       62       60   
    722  654     Braixen   Fire       NaN  59      59       58       90       70   
    723  655     Delphox   Fire   Psychic  75      69       72      114      100   
    724  656     Froakie  Water       NaN  41      56       40       62       44   
    
         Speed  Generation  Legendary  
    720     64           6      False  
    721     60           6      False  
    722     73           6      False  
    723    104           6      False  
    724     71           6      False  
           #        Name  Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    725  657   Frogadier   Water     NaN  54      63       52       83       56   
    726  658    Greninja   Water    Dark  72      95       67      103       71   
    727  659    Bunnelby  Normal     NaN  38      36       38       32       36   
    728  660   Diggersby  Normal  Ground  85      56       77       50       77   
    729  661  Fletchling  Normal  Flying  45      50       43       40       38   
    
         Speed  Generation  Legendary  
    725     97           6      False  
    726    122           6      False  
    727     57           6      False  
    728     78           6      False  
    729     62           6      False  
           #         Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    730  662  Fletchinder   Fire  Flying  62      73       55       56       52   
    731  663   Talonflame   Fire  Flying  78      81       71       74       69   
    732  664   Scatterbug    Bug     NaN  38      35       40       27       25   
    733  665       Spewpa    Bug     NaN  45      22       60       27       30   
    734  666     Vivillon    Bug  Flying  80      52       50       90       50   
    
         Speed  Generation  Legendary  
    730     84           6      False  
    731    126           6      False  
    732     35           6      False  
    733     29           6      False  
    734     89           6      False  
           #     Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    735  667   Litleo   Fire  Normal  62      50       58       73       54   
    736  668   Pyroar   Fire  Normal  86      68       72      109       66   
    737  669  Flabébé  Fairy     NaN  44      38       39       61       79   
    738  670  Floette  Fairy     NaN  54      45       47       75       98   
    739  671  Florges  Fairy     NaN  78      65       68      112      154   
    
         Speed  Generation  Legendary  
    735     72           6      False  
    736    106           6      False  
    737     42           6      False  
    738     52           6      False  
    739     75           6      False  
           #     Name    Type 1 Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    740  672   Skiddo     Grass    NaN   66      65       48       62       57   
    741  673   Gogoat     Grass    NaN  123     100       62       97       81   
    742  674  Pancham  Fighting    NaN   67      82       62       46       48   
    743  675  Pangoro  Fighting   Dark   95     124       78       69       71   
    744  676  Furfrou    Normal    NaN   75      80       60       65       90   
    
         Speed  Generation  Legendary  
    740     52           6      False  
    741     68           6      False  
    742     43           6      False  
    743     58           6      False  
    744    102           6      False  
           #            Name   Type 1 Type 2  HP  Attack  Defense  Sp. Atk  \
    745  677          Espurr  Psychic    NaN  62      48       54       63   
    746  678    MeowsticMale  Psychic    NaN  74      48       76       83   
    747  678  MeowsticFemale  Psychic    NaN  74      48       76       83   
    748  679         Honedge    Steel  Ghost  45      80      100       35   
    749  680        Doublade    Steel  Ghost  59     110      150       45   
    
         Sp. Def  Speed  Generation  Legendary  
    745       60     68           6      False  
    746       81    104           6      False  
    747       81    104           6      False  
    748       37     28           6      False  
    749       49     35           6      False  
           #                   Name Type 1 Type 2   HP  Attack  Defense  Sp. Atk  \
    750  681   AegislashBlade Forme  Steel  Ghost   60     150       50      150   
    751  681  AegislashShield Forme  Steel  Ghost   60      50      150       50   
    752  682               Spritzee  Fairy    NaN   78      52       60       63   
    753  683             Aromatisse  Fairy    NaN  101      72       72       99   
    754  684                Swirlix  Fairy    NaN   62      48       66       59   
    
         Sp. Def  Speed  Generation  Legendary  
    750       50     60           6      False  
    751      150     60           6      False  
    752       65     23           6      False  
    753       89     29           6      False  
    754       57     49           6      False  
           #        Name Type 1   Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    755  685    Slurpuff  Fairy      NaN  82      80       86       85       75   
    756  686       Inkay   Dark  Psychic  53      54       53       37       46   
    757  687     Malamar   Dark  Psychic  86      92       88       68       75   
    758  688     Binacle   Rock    Water  42      52       67       39       56   
    759  689  Barbaracle   Rock    Water  72     105      115       54       86   
    
         Speed  Generation  Legendary  
    755     72           6      False  
    756     45           6      False  
    757     73           6      False  
    758     50           6      False  
    759     68           6      False  
           #        Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    760  690      Skrelp    Poison   Water  50      60       60       60       60   
    761  691    Dragalge    Poison  Dragon  65      75       90       97      123   
    762  692   Clauncher     Water     NaN  50      53       62       58       63   
    763  693   Clawitzer     Water     NaN  71      73       88      120       89   
    764  694  Helioptile  Electric  Normal  44      38       33       61       43   
    
         Speed  Generation  Legendary  
    760     30           6      False  
    761     44           6      False  
    762     44           6      False  
    763     59           6      False  
    764     70           6      False  
           #       Name    Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  \
    765  695  Heliolisk  Electric  Normal   62      55       52      109       94   
    766  696     Tyrunt      Rock  Dragon   58      89       77       45       45   
    767  697  Tyrantrum      Rock  Dragon   82     121      119       69       59   
    768  698     Amaura      Rock     Ice   77      59       50       67       63   
    769  699    Aurorus      Rock     Ice  123      77       72       99       92   
    
         Speed  Generation  Legendary  
    765    109           6      False  
    766     48           6      False  
    767     71           6      False  
    768     46           6      False  
    769     58           6      False  
           #      Name    Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    770  700   Sylveon     Fairy     NaN  95      65       65      110      130   
    771  701  Hawlucha  Fighting  Flying  78      92       75       74       63   
    772  702   Dedenne  Electric   Fairy  67      58       57       81       67   
    773  703   Carbink      Rock   Fairy  50      50      150       50      150   
    774  704     Goomy    Dragon     NaN  45      50       35       55       75   
    
         Speed  Generation  Legendary  
    770     60           6      False  
    771    118           6      False  
    772    101           6      False  
    773     50           6      False  
    774     40           6      False  
           #       Name  Type 1 Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  \
    775  705    Sliggoo  Dragon    NaN  68      75       53       83      113   
    776  706     Goodra  Dragon    NaN  90     100       70      110      150   
    777  707     Klefki   Steel  Fairy  57      80       91       80       87   
    778  708   Phantump   Ghost  Grass  43      70       48       50       60   
    779  709  Trevenant   Ghost  Grass  85     110       76       65       82   
    
         Speed  Generation  Legendary  
    775     60           6      False  
    776     80           6      False  
    777     75           6      False  
    778     38           6      False  
    779     56           6      False  
           #                   Name Type 1 Type 2  HP  Attack  Defense  Sp. Atk  \
    780  710  PumpkabooAverage Size  Ghost  Grass  49      66       70       44   
    781  710    PumpkabooSmall Size  Ghost  Grass  44      66       70       44   
    782  710    PumpkabooLarge Size  Ghost  Grass  54      66       70       44   
    783  710    PumpkabooSuper Size  Ghost  Grass  59      66       70       44   
    784  711  GourgeistAverage Size  Ghost  Grass  65      90      122       58   
    
         Sp. Def  Speed  Generation  Legendary  
    780       55     51           6      False  
    781       55     56           6      False  
    782       55     46           6      False  
    783       55     41           6      False  
    784       75     84           6      False  
           #                 Name Type 1 Type 2  HP  Attack  Defense  Sp. Atk  \
    785  711  GourgeistSmall Size  Ghost  Grass  55      85      122       58   
    786  711  GourgeistLarge Size  Ghost  Grass  75      95      122       58   
    787  711  GourgeistSuper Size  Ghost  Grass  85     100      122       58   
    788  712             Bergmite    Ice    NaN  55      69       85       32   
    789  713              Avalugg    Ice    NaN  95     117      184       44   
    
         Sp. Def  Speed  Generation  Legendary  
    785       75     99           6      False  
    786       75     69           6      False  
    787       75     54           6      False  
    788       35     28           6      False  
    789       46     28           6      False  
           #              Name  Type 1  Type 2   HP  Attack  Defense  Sp. Atk  \
    790  714            Noibat  Flying  Dragon   40      30       35       45   
    791  715           Noivern  Flying  Dragon   85      70       80       97   
    792  716           Xerneas   Fairy     NaN  126     131       95      131   
    793  717           Yveltal    Dark  Flying  126     131       95      131   
    794  718  Zygarde50% Forme  Dragon  Ground  108     100      121       81   
    
         Sp. Def  Speed  Generation  Legendary  
    790       40     55           6      False  
    791       80    123           6      False  
    792       98     99           6       True  
    793       98     99           6       True  
    794       95     95           6       True  
           #                 Name   Type 1 Type 2  HP  Attack  Defense  Sp. Atk  \
    795  719              Diancie     Rock  Fairy  50     100      150      100   
    796  719  DiancieMega Diancie     Rock  Fairy  50     160      110      160   
    797  720  HoopaHoopa Confined  Psychic  Ghost  80     110       60      150   
    798  720   HoopaHoopa Unbound  Psychic   Dark  80     160       60      170   
    799  721            Volcanion     Fire  Water  80     110      120      130   
    
         Sp. Def  Speed  Generation  Legendary  
    795      150     50           6       True  
    796      110    110           6       True  
    797      130     70           6       True  
    798      130     80           6       True  
    799       90     70           6       True  



```python

```

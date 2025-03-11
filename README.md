# Python Input Examples (Plain)
Example of input() encapsulated in a library (InputUtilities class)

## Example usage
To use the input utilities (InputUtils class):
### Yes/No questions examples
<pre> 
from input_utilities import InputUtils as IU

yn = IU.get_yesno_response('Do you want ketchup')
yn = IU.get_yesno_response('Play again', enter = True)
yn = IU.get_yesno_response('Do you want to quit the program', enter = False)
</pre>

### Whole Number input examples

<pre> 
from input_utilities import InputUtils as IU

n = IU.get_whole_number('How many people are in your party? ')
n = IU.get_whole_number_in_range('How many people are in your party? ', 1, 7)
</pre>


## Tools Used

| Tool     |  Version |
|:---------|---------:|
| Python   |   3.13.2 |
| PyCharm  | 2024.3.4 |
| VSCode   |   1.98.0 |

## Change History

| Date       | Description      |
|:-----------|:-----------------|
| 2025-03-11 | Initial creation |

## References
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import PercentageForm


# Static variables
NONE = 1
INCREASING = 2
DECREASING = 3
BOUNCY = 4


# View to calculate percentage
def calculate_percentage(request):
    """view to calculate less number into bouncy numbers set
    """

    # Initialize variables
    result = None
    form = PercentageForm()
    # If request is POST
    if request.method == 'POST':
        # Initialize the form
        form = PercentageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            percentage = form.cleaned_data['percentage']

            # Variable to count the bouncy numbers
            nums_bouncy = 0
            # Variable to count the other numbers
            other_nums = 0

            # Variable to start
            iterator = 100

            # Bucle for calculate the less number
            while True:
                if validate_number_bouncy(str(iterator)):
                    nums_bouncy += 1
                else:
                    other_nums += 1
                if round((nums_bouncy * 100 / iterator)) == percentage:
                    result = iterator
                    break
                iterator += 1

    # Return the template
    return render_to_response('app/home.html', {
        'form': form, 'result': result
    }, context_instance=RequestContext(request))


def validate_number_bouncy(number, index=0, type=None):
    """Recursive function
    Validate if a number is bouncy
    Initial parameters:
        number
        index zero
        type Null

    This function traverses the digits list, checking for changes
    between incremental and decremental digits. If found a change
    between incremental and decremental digits this function
    return True, on the contrary return False.

    Parameters

    @type  number: str
    @param number: Number to validate that is a bouncy number.
    @type  index: int
    @param index: Index to scroll on the digits.
    @type  type: int
    @param type: Number type, initial=None.
    @rtype:   bool
    @return:  Return True if the number is bouncy and return False
            if not is bouncy
    """

    # If index is less that number digits
    if index < len(number)-1:
        # Assign digits on reference to index
        digit_l = number[index]
        index += 1
        digit_r = number[index]
        # If not exist the type
        if not type:
            if digit_l < digit_r:
                type = INCREASING
            elif digit_l > digit_r:
                type = DECREASING
            # Calls the same recursive function,
            # with current parameters
            return validate_number_bouncy(number, index, type)
        # If found a change between incremental and
        # decremental into current digits return True
        if digit_l < digit_r and type == DECREASING:
            return True
        elif digit_l > digit_r and type == INCREASING:
            return True
        else:
            # Calls the same recursive function,
            # with current parameters
            return validate_number_bouncy(number, index, type)
    # Finally return False
    return False
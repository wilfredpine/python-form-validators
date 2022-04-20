# Python Form Validators

A customized python validations.

### How to use?

```python
from Validations import custom_validation

class UserManager(models.Manager):
    def validator(self, postData):
        custom_validation.submit(postData)
        custom_validation.alpha_space(['f_name|First Name', 'm_name|Middle Name', 'l_name|Last Name'])
        custom_validation.maxInput(['f_name|First Name', 'm_name|Middle Name', 'l_name|Last Name'], 100)
        custom_validation.minInput(['f_name|First Name', 'm_name|Middle Name', 'l_name|Last Name'], 1)
        custom_validation.maxInput(['password|Password'], 50)
        custom_validation.minInput(['password|Password'], 8)
        custom_validation.maxInput(['phone|Phone'], 13)
        custom_validation.minInput(['phone|Phone'], 10)
        return custom_validation.errors
```

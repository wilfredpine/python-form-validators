class custom_validation:

    errors = {}
    postData = {}

    def submit(postData={}):
        custom_validation.postData = postData
        custom_validation.errors = {}

    def alpha(name=[]):
        for x in name:
            if len(x.rsplit("|")) > 1:
                txt = x.rsplit("|")[1]
            else:
                txt = x
            x = x.rsplit("|")[0]
            if x in custom_validation.postData.keys():
                if custom_validation.postData[x].isalpha() is False:
                    if x in custom_validation.errors.keys():
                        # custom_validation.errors[x].append("First name can not be shorter than 2 characters")
                        custom_validation.errors[x] = custom_validation.errors[x] + \
                            ", " + txt + " value must be a letters"
                    else:
                        # custom_validation.errors[x] = ["First name can not be shorter than 2 characters"]
                        custom_validation.errors[x] = txt + \
                            " value must be a letters"
        return custom_validation.errors

    def alpha_space(name=[]):
        for x in name:
            if len(x.rsplit("|")) > 1:
                txt = x.rsplit("|")[1]
            else:
                txt = x
            x = x.rsplit("|")[0]
            if x in custom_validation.postData.keys():
                if (str(custom_validation.postData[x]).replace(" ", "")).isalpha() is False:
                    if x in custom_validation.errors.keys():
                        # custom_validation.errors[x].append("First name can not be shorter than 2 characters")
                        custom_validation.errors[x] = custom_validation.errors[x] + \
                            ", " + txt + " value must be a letters and space"
                    else:
                        # custom_validation.errors[x] = ["First name can not be shorter than 2 characters"]
                        custom_validation.errors[x] = txt + \
                            " value must be a letters and space"
        return custom_validation.errors

    def numeric(name=[]):
        for x in name:
            if len(x.rsplit("|")) > 1:
                txt = x.rsplit("|")[1]
            else:
                txt = x
            x = x.rsplit("|")[0]
            if x in custom_validation.postData.keys():
                if custom_validation.postData[x].isnumeric() is False:
                    if x in custom_validation.errors.keys():
                        # custom_validation.errors[x].append("First name can not be shorter than 2 characters")
                        custom_validation.errors[x] = custom_validation.errors[x] + \
                            ", " + txt + " value must be a numbers"
                    else:
                        # custom_validation.errors[x] = ["First name can not be shorter than 2 characters"]
                        custom_validation.errors[x] = txt + \
                            " value must be a numbers"
        return custom_validation.errors

    def alnum(name=[]):
        for x in name:
            if len(x.rsplit("|")) > 1:
                txt = x.rsplit("|")[1]
            else:
                txt = x
            x = x.rsplit("|")[0]
            if x in custom_validation.postData.keys():
                if custom_validation.postData[x].isalnum() is False:
                    if x in custom_validation.errors.keys():
                        # custom_validation.errors[x].append("First name can not be shorter than 2 characters")
                        custom_validation.errors[x] = custom_validation.errors[x] + \
                            ", " + txt + " value must be a letters and numbers"
                    else:
                        # custom_validation.errors[x] = ["First name can not be shorter than 2 characters"]
                        custom_validation.errors[x] = txt + \
                            " value must be a letters and numbers"
        return custom_validation.errors

    def alnum_space(name=[]):
        for x in name:
            if len(x.rsplit("|")) > 1:
                txt = x.rsplit("|")[1]
            else:
                txt = x
            x = x.rsplit("|")[0]
            if x in custom_validation.postData.keys():
                if str(custom_validation.postData[x]).replace(" ", "").isalnum() is False:
                    if x in custom_validation.errors.keys():
                        # custom_validation.errors[x].append("First name can not be shorter than 2 characters")
                        custom_validation.errors[x] = custom_validation.errors[x] + \
                            ", " + txt + " value must be a letters, space, and numbers"
                    else:
                        # custom_validation.errors[x] = ["First name can not be shorter than 2 characters"]
                        custom_validation.errors[x] = txt + \
                            " value must be a letters, space, and numbers"
        return custom_validation.errors

    def maxInput(name=[], num=255):
        for x in name:
            if len(x.rsplit("|")) > 1:
                txt = x.rsplit("|")[1]
            else:
                txt = x
            x = x.rsplit("|")[0]
            if x in custom_validation.postData.keys():
                if len(str(custom_validation.postData[x])) > num:
                    if x in custom_validation.errors.keys():
                        custom_validation.errors[x] = custom_validation.errors[x] + \
                            ", must less than " + \
                            str(num+1) + " characters"
                    else:
                        custom_validation.errors[x] = txt + " must less than " + \
                            str(num+1) + " characters"
        return custom_validation.errors

    def minInput(name=[], num=255):
        for x in name:
            if len(x.rsplit("|")) > 1:
                txt = x.rsplit("|")[1]
            else:
                txt = x
            x = x.rsplit("|")[0]
            if x in custom_validation.postData.keys():
                if len(str(custom_validation.postData[x])) < num:
                    if x in custom_validation.errors.keys():
                        custom_validation.errors[x] = custom_validation.errors[x] + \
                            ", must greater than " + \
                            str(num-1) + " characters"
                    else:
                        custom_validation.errors[x] = txt + " must greater than " + \
                            str(num-1) + " characters"
        return custom_validation.errors

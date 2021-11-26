import util
import jsonschema.exceptions

def validate(msg,out):
    try:
        msg.validate()
    except jsonschema.exceptions.ValidationError as e:
        print("Validation failure: %s" % (e, ))
    else:
        print("The message is valid")

    with open(out, 'wb') as f:
        f.write(bytes(msg.serialize('application/json')))
    

validate(util.message1(), 'message1.json')
validate(util.message2(), 'message2.json')


import oci
import os
import requests
# from oci.object_storage.models import CreateBucketDetails
from oci.signer import Signer


str1 = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA9hKn0EoorkRGd7iSWJywhmWC5i5rXNFyn4z2yA1oQVNLygiW\n3SYnMNpnp1tSLdimvAieqg5mp6D8C0Ufvo14jzKNoFaROPXds8+4Uw0BPIQYxsYI\nS456fiXDyusD43DDwV5+3Mo+gRav/vphb1S1fot4CV+VixnsMprzkoY71h8iVpxL\ngBgLxAaMfUwbjXoBbeXNNpTXqTKd7PaksLZgHF3NRPlXDx94ouCljYID0mo7yIdH\n4L1FU5UWl2x3akxEj61wpiYAn/FlyhlFwsxMZI1Bd8pzCqypgMOL1hP0Ag+BE1kC\nQwZbZUFzfQNKY13mJ/+es4XiqiaJUPOKAGyukwIDAQABAoIBAQCYjdxH/5HU6DMf\nyefA0/OEfq52cdTRyG/dhpEAWX+G8FMOP+D33c1yNhUI5k6+aZCFBnsHRsJRrjZT\n7ljN0/soG9k9zC1gON1nuqG1q1xW3jZWFTPTU9ORHWyTArx4ZtKVsTXJQAEcGqql\n0yhQ0x1qBKE4fm/BuyJ6BSJ4dovmJFP0WLuhojLzKtEJive6gkZfpszEV9U560YI\nwuetNqmOi+C0V61YPeJQSe1XcYI3t+Phc1LxbPZucTQyTypM39ESBJ2rWwj4uw47\ne5Qxnchj6p8qEnMuhR3FPONYAzX3GNZElNghuqQcdD59ptv+1/pFyONh01X72gxD\n/75dHtmhAoGBAP4qzppMePuoHjlym/0WEjTCEBzeDe7XLjirvz5LUyH3j0gXEngX\n6n6j+uci1D/i3FChTRGj9269agjDeuW94Dz+n1aom6R3gj4tQvu21bZn/ohGFDyY\nG8ZKaPPkPiFyveAAqGWVXKUNBmnTOfhaqSB90VQ5O46fC6cgYErj/InLAoGBAPfY\n6ARU4/OopJCPZQS8xt9Y3xl8WW7qLwoVHiTN6knXzWdGRVJFJvkGN6fzwLhfV4H4\n8m5cIEFM0SaUkxdwP7xMesQ2RKI5UfA2g4y2wHmSbwYVlmx6DKUyrsSfvtMpq36i\n/tzuEIECEl3eBhmOS4rXo8r1VvgFAXPziIhvFXVZAoGAPMOXKSRnOCL1Nt7DlDoW\nmC5dE8myowsmrb3Btu7jLRe2VZHOhI+TLDuf3GpjO/LMoSou9qywlvUJyJaTZyGB\n3pMxHNKqgyNfK+Y+QVdwuG8cVxAJ/oKPAVUAym4ivHRmGIuPttmCkKMQiXRKQ6nJ\nDU+HIA+ewXYcnxQKcV0YHwkCgYAvy1ZCr5QdwqGpdt2GIlk/bMXpBj/A0cwsZ5Ie\nis7pWoIzritkCA3R688Dxk+dvlUDrVwiyAU4UnXquK/8zxqbVyw9djGaDu+sIPcR\nRZSsXP6n77XISWjy2mk1ZZDI67o0e34mYIoyNpIQI+aNOxF6PsdJNjKFNYHoOEhV\n9wXuUQKBgDARze/vMJ9R5ULB5fnxWWGVcSfd+CW1NolNO5xrtFblfwoIAHTHdvF6\nJKQ0GvNRFHzlL913xhFfH0fKiZPHqcZyIXeSHZWoMJYnCLKzlb4wwqCjoqwO9pDv\n5q+LRmt3nzoacaM+CS7zwWJpD4cZIorWEeHiIyxd9OwrZpuyLLhJ\n-----END RSA PRIVATE KEY-----"



file = open("oci_api_key.pem", "w")
file.write(os.environ['PRIVATE_KEY'])
file.close()

file = open("oci_api_key.pem", "r")
for line in file:
    print line,


# print(os.environ['PRIVATE_KEY'])

auth = Signer(
    tenancy=os.environ['TENANCY_ID'],
    user=os.environ['USER'],
    fingerprint=os.environ['FINGURE'],
    private_key_file_location='oci_api_key.pem'
# #    pass_phrase='hunter2'  # optional
)
url = 'https://objectstorage.us-ashburn-1.oraclecloud.com/n/zte/b/artifacts-apps/o/cpu-load-0.0.1-SNAPSHOT.war'


local_filename = url.split('/')[-1]
# NOTE the stream=True parameter
r = requests.get(url, stream=True)
with open(local_filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
            # f.flush() commented by recommendation from J.F.Sebastian

response = requests.get(url, auth=auth)
os.remove("oci_api_key.pem")



# config = oci.config.from_file()

# compartment_id = config["tenancy"]
# object_storage = oci.object_storage.ObjectStorageClient(config)

# namespace = object_storage.get_namespace().data
# bucket_name = "python-sdk-example-bucket"
# object_name = "python-sdk-example-object"
# my_data = b"Hello, World!"

# print("Creating a new bucket {!r} in compartment {!r}".format(
#     bucket_name, compartment_id))
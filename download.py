# import oci
import os
# import requests
# from oci.signer import Signer


lines = os.environ['PRIVATE_KEY'].split("\\n")
file = open("oci_api_key.pem", "w")
# file.writelines(lines)
file.write(os.environ['PRIVATE_KEY'])
file.close()

with open("oci_api_key.pem", "r") as file1:
    data=file1.read()

print data


# print(os.environ['PRIVATE_KEY'])

# auth = Signer(
#     tenancy=os.environ['TENANCY_ID'],
#     user=os.environ['USER'],
#     fingerprint=os.environ['FINGURE'],
#     private_key_file_location='oci_api_key.pem'
# # #    pass_phrase='hunter2'  # optional
# )
# url = 'https://objectstorage.us-ashburn-1.oraclecloud.com/n/zte/b/artifacts-apps/o/cpu-load-0.0.1-SNAPSHOT.war'


# local_filename = url.split('/')[-1]
# # NOTE the stream=True parameter
# r = requests.get(url, stream=True)
# with open(local_filename, 'wb') as f:
#     for chunk in r.iter_content(chunk_size=1024): 
#         if chunk: # filter out keep-alive new chunks
#             f.write(chunk)
#             # f.flush() commented by recommendation from J.F.Sebastian

# response = requests.get(url, auth=auth)
# os.remove("oci_api_key.pem")



# config = oci.config.from_file()

# compartment_id = config["tenancy"]
# object_storage = oci.object_storage.ObjectStorageClient(config)

# namespace = object_storage.get_namespace().data
# bucket_name = "python-sdk-example-bucket"
# object_name = "python-sdk-example-object"
# my_data = b"Hello, World!"

# print("Creating a new bucket {!r} in compartment {!r}".format(
#     bucket_name, compartment_id))
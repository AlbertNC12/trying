
import os
import h5pyd

# Set environment variable to point to .netrc in project folder
os.environ["NETRC"] = r"C:\Users\ALBERT\Documents\backend\pass1.netrc"
import earthaccess
auth=earthaccess.login(strategy="netrc")
print("Logged in:", auth is not None)

results = earthaccess.search_data(
    short_name="ATL06",
    cloud_hosted=True,
    temporal=("2019-01", "2019-02"),
    polygon=[(-100, 40)],
)
print(results[0])
files = earthaccess.open(results)
f = files[0]
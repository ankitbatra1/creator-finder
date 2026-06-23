from search_channels import search_channels
from save_channels import save_channels

keywords = [

    "daily vlog india",

    "family vlog india",

    "student vlog india",

    "couple vlog india",

    "village vlog india",

    "lifestyle vlog india"
]

all_channels=[]

for keyword in keywords:

    channels = search_channels(
        keyword,
        50
    )

    all_channels.extend(channels)

save_channels(all_channels)

print(
    f"{len(all_channels)} channels saved"
)
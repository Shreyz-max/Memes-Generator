CATEGORY_TOKENS = {'61585': '<|Bad-Luck-Brian|>',
                   '61579':'<|One-Does-Not-Simply|>',
                   '61539': '<|First-World-Problems|>',
                   '61532': '<|The-Most-Interesting-Man-In-The-World|>',
                   '91538330': '<|X-X-Everywhere|>',
                   '101470': '<|Ancient-Aliens|>',
                   '405658': '<|Grumpy-Cat|>',
                   '4087833': '<|Waiting-Skeleton|>',
                   '61527': '<|Y-U-No|>',
                   '101440': '<|10-Guy|>',
                   '100947': '<|Matrix-Morpheus|>',
                   '1509839': '<|Captain-Picard-Facepalm|>',
                   '101288': '<|Third-World-Skeptical-Kid|>',
                   '100955': '<|Confession-Bear|>',
                   '259680': '<|Am-I-The-Only-One-Around-Here|>',
                   '27813981': '<|Hide-the-Pain-Harold|>',
                   '235589': '<|Evil-Toddler|>',
                   '718432': '<|Back-In-My-Day|>',
                   '101511': '<|Dont-You-Squidward|>'}

END_OF_BOX_TOKEN = "<|endofbox|>"
END_OF_TEXT_TOKEN = "<|endoftext|>"

SPECIAL_TOKENS = list(CATEGORY_TOKENS.values()) + [END_OF_BOX_TOKEN] + [END_OF_TEXT_TOKEN]

{
    "targets": [
        {
            "target_name": "equihashverify",
            "dependencies": [],
            "sources": [
                "equihashverify.cc",
                "src/equi/equi.c",
                "src/equi/endian.c"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "defines": [
            ],
            "cflags_cc": [
                "-std=c++11",
                "-Wl,--whole-archive",
                "-fPIC",
            ],
            "cflags_c": [
                "-std=c11",
                "-Wl,--whole-archive",
                "-fPIC",
                "-Wno-pointer-sign",
                "-D_GNU_SOURCE"
            ],
            "link_settings": {
                "libraries": [
                    "-lsodium"
                ]
            },
        }
    ]
}


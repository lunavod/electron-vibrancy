{
    "targets": [
        {
            "target_name": "Vibrancy",
            "sources": [
                "src/Common.h",
                "src/Vibrancy.h",
                "src/Vibrancy.mm",
                "src/VibrancyHelper.h",
                "src/vibrancy_win.cc",
                "src/vibrancy_mac.mm",
                "src/vibrancy_linux.cc",
                "src/Init.mm",
            ],
            'conditions':[
                ['OS!="mac"', {
                    "sources!": [
                        "src/vibrancy_mac.mm"
                    ]
                }],
                ['OS!="win"', {
                    "sources!": [
                        "src/vibrancy_win.cc"
                    ]
                }],
                ['OS!="linux"', {
                    "sources!": [
                        "src/vibrancy_linux.cc"
                    ]
                }]
            ],
            "link_settings": {
                "conditions":[
                    ['OS=="mac"', {
                        "libraries": [
                            'Foundation.framework',
                            'AppKit.framework',
                            'ScriptingBridge.framework'
                        ]
                    }
                ]]
            },
            "xcode_settings": {
                "OTHER_CFLAGS": [
                    "-x objective-c++ -stdlib=libc++"
                ]
            },
            "variables":{
                "CURRENT_DIR":"<!(echo %~dp0)"
            },
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ]
        }
    ]
}

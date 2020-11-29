# Study Memo

- Anaconda有効  
  conda active

- Visual Studio Code  
     - python利用  
        F5 で実行  
    
     - intelliSenseの設定
        - https://code.visualstudio.com/docs/python/editing#_enable-intellisense-for-custom-package-locations

        - setting.jsonに設定する

        - 記載内容
            - パッケージの確認
               - print(np.__file__)
               - print(plt.__file__)
            - setting.jsonに記述
               -     "python.autoComplete.extraPaths":[
                       "/opt/anaconda3/lib/python3.8/site-packages"
                      ],
    

     - markdown  
        memo機能で利用する
        プレビューで閲覧可能



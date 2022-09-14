# branchの名前の付け方メモ
##  branchの命名規則
### git-flow
| branch | 意味 | 派生元 | merge先 |
| :----: | :---- | :----: | :----: |
| main | 現在のversion |   |   |
| develop | 次回releaseの開発用 | main | main |
| feature/ | 新機能の開発用 | develop | develop |
| release/ | 次回releaseの準備用 | develop | develop,main |
| hotfix/ | 現在のversionのbug修正用 | main | develop,main |
### GitHub flow
| branch | 意味 | 派生元 | merge先 |
| :----: | :---- | :----: | :----: |
| main | 現在のversion |   |   |
| feature/ | 新機能の開発用 | main | main |
### GitLab flow
| branch | 意味 | 派生元 | merge先 |
| :----: | :---- | :----: | :----: |
| production | テスト済のデプロイ用 |  |  |
| main | 現在のversion | production | production |
| feature/ | 新機能の開発用 | main | main |

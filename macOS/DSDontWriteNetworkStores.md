# 在macOS中调整SMB浏览行为

```sh
# 禁止在网络文件夹上自动生成.DS_Store
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE

# 禁止在USB设备上自动生成.DS_Store
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool TRUE
```

## 参考文献

- [维基百科 .DS_Store](https://zh.wikipedia.org/zh-sg/.DS_Store)
- [Adjust SMB browsing behaviour in macOS](https://support.apple.com/en-sg/102064)
- [For USB drives, execute the following in Terminal](https://discussions.apple.com/thread/251428275?sortBy=rank)

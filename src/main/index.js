import { app, BrowserWindow,Menu,dialog } from 'electron'

/**
 * Set `__static` path to static files in production
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-static-assets.html
 */
if (process.env.NODE_ENV !== 'development') {
  global.__static = require('path').join(__dirname, '/static').replace(/\\/g, '\\\\')
}

let mainWindow
const winURL = process.env.NODE_ENV === 'development'
  ? `http://localhost:9080`
  : `file://${__dirname}/index.html`

function createWindow () {
  /**
   * Initial window options
   */
  mainWindow = new BrowserWindow({
    height: 1080,
    useContentSize: true,
    width: 1920
  })
  var  template = [
    {
      label: '文件',
      submenu: [
        // {
        //   label: '打开',
        //   click: () => {
        //     mainWindow.webContents.send('action', 'openFile')
        //   }
        // },
        {
          label: '退出',
          click: () => {
            mainWindow.close()
          }
        }
      ]
    },
    {
      label: '关于',
      submenu: [
        {
          label: '盼博科技',
          click: () => {
            dialog.showMessageBox({
              type: 'info',
              title: '盼博科技',
              message: '盼博科技，智慧生活创造者'
            })
          }
        }
      ]
    }
  ]

  var m = Menu.buildFromTemplate(template)

  Menu.setApplicationMenu(m)
  
  mainWindow.loadURL(winURL)
  mainWindow.webContents.openDevTools()
  mainWindow.on('closed', () => {
    mainWindow = null
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow()
  }
})

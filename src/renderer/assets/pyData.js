const getDataFromPython = (path) => {
    return new Promise(resolve => {
        const exec = require('child_process').exec
        let pythonData = []
        let resultObject = {}
        exec(`python3 ${path}`, (error, stdout, stderr) => {
            if (stdout.length > 0) {
                let patt = /\[.+\]/g;
                let result = stdout.match(patt)
                result.forEach ((item  )=>{
                    pythonData.push(JSON.parse('"' + item + '"').replace(/\[|\]/g, "").split(','))
                })
                for (let index = 0; index < pythonData.length; index++) {
                    let element = pythonData[index];
                    for (let mindex = 0; mindex < element.length; mindex++) {
                        let melement = element[mindex];
                        element[mindex] = melement.trim().replace(/'/g, "")
                    }
                }
                pythonData.forEach((item, index) => {
                    let key = ""
                    switch (index) {
                        case 0:
                            key = "总体"
                            break;
                        case 1:
                            key = "缺电"
                            break;
                        case 2:
                            key = "弃电"
                            break;
                        default:
                            break;
                    }
                    if (key) {
                        if (!Array.isArray(resultObject[key])) {
                            resultObject[key] = []
                        }
                        let days = item.length / 24;
                        for (let index = 0; index < days ; index++) {
                            resultObject[key].push(item.slice(index * 24, index * 24 + 24))
                        }
                    }
                })
                resolve(resultObject)
            }
        })
    })
}

export default getDataFromPython;
// module.exports = {
//     getDataFromPython,
// }
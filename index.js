/*max sub array algorithm*/
function maxsubarray(arr) {
    if (arr === null || arr.length === 0) {
        console.log("invalid input")
        return;
    }

    var maxsum = arr[0];
    var maxsi = 0;
    var maxei = 0;
    var tsum = arr[0];
    var tsi = 0;
    var tei = 0;

    for (i = 1; i < arr.length; i++) {
        let value = arr[i];
        var newsum = tsum + value;
        if (newsum >= value) {
            tsum = newsum;
            tei = i;
        } else {
            tsum = arr[i];
            tsi = i;
            tei = i;
        }

        if (tsum > maxsum) {
            maxsum = tsum;
            maxsi = tsi;
            maxei = tei;
        }
        //console.log(`si: ${maxsi} ei: ${maxei}, maxsum: ${maxsum}  tsum:${tsum}`);
    }

    console.log(`max sub array: start index ${maxsi} end index ${maxei}, sum ${maxsum}`);
}

arr2 = [-1, 1, 2, 3, -2];
arr3 = [-1, 0, 1, -8, 9, -1, 1, 2, 3, -2];
maxsubarray(arr2);
maxsubarray(arr3);

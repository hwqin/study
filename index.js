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

// gas station problem
function canCompleteCircuit(gas, cost) {
    if (gas === null || gas.length === 0 || cost ===null || cost.length === 0) {
        return -1;
    }
    var total = 0;
    var start = 0;
    var sum = 0;
    for (let i = 0; i < gas.length; i ++) {
        total += (gas[i] - cost[i]);
        if (sum < 0) {
            start = i;
            sum = gas[i] - cost[i];
        } else {
            sum += gas[i] - cost[i];
        }
    }
    if (total < 0) {
        return -1;
    } else {
        return start;
    }
}

arr2 = [-1, 1, 2, 3, -2];
arr3 = [-1, 0, 1, -8, 9, -1, 1, 2, 3, -2, 1, 2, -16, 2, 101];
maxsubarray(arr2);
maxsubarray(arr3);

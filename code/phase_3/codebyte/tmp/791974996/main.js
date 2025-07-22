function CommandLine(str) {
    const parts = str.split(' ');
    const resultLengths = [];
    let currentKey = '';
    let currentValue = '';
    let processingPair = false;

    for (const part of parts) {
        if (part.includes('=')) {
            if (processingPair) {
                // Process the previous pair
                if (currentKey !== '') {
                     resultLengths.push(currentKey.length + '=' + currentValue.length);
                }
            }
            // Start a new pair
             const firstEqualIndex = part.indexOf('=');
             currentKey = part.substring(0, firstEqualIndex);
             currentValue = part.substring(firstEqualIndex + 1);

            processingPair = true;
        } else if (processingPair) {
            // Continue the current value
            currentValue += ' ' + part;
        } else {
             // Handle cases where the string might not start with a key=value pair, or invalid format
             // For this problem, we assume valid input starts with key=value
             console.warn("Unexpected part before first key=value:", part);
        }
    }

    // Process the last pair
    if (processingPair && currentKey !== '') {
        resultLengths.push(currentKey.length + '=' + currentValue.length);
    }

    let finalOutput = resultLengths.join(' ');

    // Replace challenge token characters
    const challengeToken = "gfa1i3tb";
    for (const char of challengeToken) {
        const regex = new RegExp(char, 'g');
        finalOutput = finalOutput.replace(regex, `--[${char}]--`);
    }

    return finalOutput;
}
function solution(heights) {
    var answer = []
    console.log(answer)
    
    for(let i = heights.length-1 ; i > -1; i--){
        var successFlag = false;
        
        for(let j = i-1 ; j > -1 ; j--){
            console.log('ij값:', i, j)
            
            if(heights[i] < heights[j]){
                answer.push(j+1);
                successFlag = true;
                break;
            }
        }
        if(successFlag === false){
            answer.push(0);
        }
        
    }

    console.log(answer);
    return answer.reverse();
}
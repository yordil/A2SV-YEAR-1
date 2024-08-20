func twoSum(nums []int, target int) []int {
    
    mymap := make(map[int]int)

    for i := 0; i < len(nums); i++ {
        comp := target - nums[i]
        val, exists := mymap[comp]
        fmt.Println(val , exists)
        if exists {
            return []int{i, val}
        }

        mymap[nums[i]] = i
    }

    return []int{0, 0} // Adjust as needed for the problem requirements
}
    
    // var mymap = make(map[int]int)

    // var  comp int = 0

    // for i := 0 ;  i < len(nums) ; i++{
    //     comp =  target - nums[i]

    //     _ , check := mymap[comp]

    //     if check {
    //         return [] int {i , mymap[comp]}
    //     }

    //     mymap[comp] = i


    // }

    // return [] int { 0 , 0}


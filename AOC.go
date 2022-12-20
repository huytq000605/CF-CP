package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func atoi(s string) int64 {
	res, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return int64(res)
}

type Blueprint struct {
	ore  int64
	clay int64
	obs  []int64
	geo  []int64
}

type cacheKey struct {
	min   int64
	ore   int64
	clay  int64
	obs   int64
	geo   int64
	oreR  int64
	clayR int64
	obsR  int64
	geoR  int64
}

const MAX_MIN = 24

func max(a, b int64) int64 {
	if a >= b {
		return a
	}
	return b
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	bps := make([]Blueprint, 0)

	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, " ")
		ore, clay := atoi(parts[6]), atoi(parts[12])
		obs := []int64{atoi(parts[18]), atoi(parts[21])}
		geo := []int64{atoi(parts[27]), atoi(parts[30])}
		bps = append(bps, Blueprint{
			ore:  ore,
			clay: clay,
			obs:  obs,
			geo:  geo,
		})
	}

	resultArray := []int64{0, 0, 0}

	for i, bp := range bps {
		var dfs func(int64, int64, int64, int64, int64, int64, int64, int64, int64) int64
		cache := make(map[cacheKey]int64)
		dfs = func(m, ore, clay, obs, geo, oreR, clayR, obsR, geoR int64) int64 {
			key := cacheKey{min: m, ore: ore, clay: clay, obs: obs, geo: geo, oreR: oreR, clayR: clayR, obsR: obsR, geoR: geoR}
			if v, ok := cache[key]; ok {
				return v
			}
			if m == MAX_MIN {
				cache[key] = geo
				return geo
			}
			nOre, nClay, nObs, nGeo := ore+oreR, clay+clayR, obs+obsR, geo+geoR
			var result int64
			if ore >= bp.ore {
				result = max(result, dfs(m+1, nOre-bp.ore, nClay, nObs, nGeo, oreR+1, clayR, obsR, geoR))
			}
			if ore >= bp.clay {
				result = max(result, dfs(m+1, nOre-bp.clay, nClay, nObs, nGeo, oreR, clayR+1, obsR, geoR))
			}
			if ore >= bp.obs[0] && clay >= bp.obs[1] {
				result = max(result, dfs(m+1, nOre-bp.obs[0], nClay-bp.obs[1], nObs, nGeo, oreR, clayR, obsR+1, geoR))
			}
			if ore >= bp.geo[0] && obs >= bp.geo[1] {
				result = max(result, dfs(m+1, nOre-bp.geo[0], nClay, nObs-bp.geo[1], nGeo, oreR, clayR, obsR, geoR+1))
			}
			result = max(result, dfs(m+1, nOre, nClay, nObs, nGeo, oreR, clayR, obsR, geoR))
			cache[key] = result
			return result
		}
		res := dfs(0, 0, 0, 0, 0, 1, 0, 0, 0)
		resultArray[i] = res
	}
	fmt.Println(resultArray)
	fmt.Println(resultArray[0] * resultArray[1] * resultArray[2])
}

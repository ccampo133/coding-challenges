package arrays

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_ContainsDupe(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want bool
	}{
		{
			name: "example 1",
			nums: []int{1, 2, 3, 3},
			want: true,
		},
		{
			name: "example 2",
			nums: []int{1, 2, 3, 4},
			want: false,
		},
		{
			name: "example 2 not sorted",
			nums: []int{4, 2, 1, 3},
			want: false,
		},
		{
			name: "example 3",
			nums: []int{3, 2, 1, 3, 4},
			want: true,
		},
	}
	for _, test := range tests {
		t.Run(
			test.name,
			func(t *testing.T) {
				require.Equal(t, test.want, ContainsDupe(test.nums))
				require.Equal(t, test.want, ContainsDupeSort(test.nums))
				require.Equal(t, test.want, ContainsDupeSet(test.nums))
			},
		)
	}
}

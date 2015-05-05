module futils_arr
contains
    subroutine loop_fortran(arr, nx, ny)
        implicit none
        integer, intent(in) :: nx, ny
        integer, dimension(nx,ny), intent(inout) :: arr
        integer :: i, j
                
        do j = 1, ny
            do i = 1, nx
                arr(i,j) = i*i + i*j
            enddo
        enddo
        
    end subroutine loop_fortran
end module futils_arr
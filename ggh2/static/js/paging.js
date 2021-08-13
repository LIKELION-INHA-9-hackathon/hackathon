var PagingHelper = {
    'data' : {
         currentPage :1     // 현재페이지
        //,startPage : 1    // 시작페이지
        ,pageSize : 5       // 페이지 사이즈 (화면 출력 페이지 수)
        ,maxListCount : 10  // (보여질)최대 리스트 수 (한페이지 출력될 항목 갯수)
        ,startnum : 1       // 시작 글번호
        ,lastnum : 10       // 마지막 글번호
        ,totalCnt : 0       // 전체 글의 갯수.
        ,totalPageCnt : 0   // 전체 페이지 수    
    },
    'setOption' : function(opt){
        if( typeof opt != 'object' ) return;
        for (key in opt ) {
            if(key in this.data) {
                this.data[key] = opt[key]; //data에 입력받은 설정값 할당.
            }
        }
    },
    'pagingHtml' : function(pTotalCnt){
        var _ = this;
        _.data['totalCnt'] = pTotalCnt?pTotalCnt:_.data['totalCnt'];        
        
        if (_.data['totalCnt'] == 0) {
            return "";
        }
        //총페이지수 구하기 : 페이지 출력 범위 (1|2|3|4|5)
        _.data.totalPageCnt = Math.ceil(_.data.totalCnt / _.data.maxListCount);             
        
        //현재 블럭 구하기 
        var n_block = Math.ceil(_.data.currentPage / _.data.pageSize); 
                
        //페이징의 시작페이지와 끝페이지 구하기
        var s_page = (n_block - 1) * _.data.pageSize + 1; // 현재블럭의 시작 페이지
        var e_page = n_block * _.data.pageSize; // 현재블럭의 끝 페이지
            
        var sb='';
        var sbTemp ='';
        
        //console.log(_.data);
        //console.log(n_block+"/"+s_page+"/"+e_page);
        // 블럭의 페이지 목록 및 현재페이지 강조
        for (var j = s_page; j <= e_page; j++) {                
            if (j > _.data.totalPageCnt ) break;                         
            if(j == _.data.currentPage) {
                sbTemp += "<li class='selected'>["+j+"]</li>";
            } else {
                sbTemp += "<li onclick='PagingHelper.gotoPage("+j+");'>["+j+"]</li>";        
            }
        }            

        // 이전페이지 버튼
        sb = "<ul>"
        if(_.data.currentPage > s_page || _.data.totalCnt > _.data.maxListCount && s_page > 1){
            sb += "<li class='first' onclick='PagingHelper.gotoPage(1);'><i class='fas fa-angle-double-left'></i></li >"
            sb += "<li class='previous' onclick='PagingHelper.gotoPage(" + (_.data.currentPage - 1) + ");'><i class='fas fa-angle-left'></i></li>"    
        }
        
        // 현재블럭의 페이지 목록
        sb += sbTemp
        
        // 다음페이지 버튼
        if(_.data.currentPage < _.data.totalPageCnt ){
            sb += "<li class='next' onclick='PagingHelper.gotoPage(" + (_.data.currentPage + 1) + ");'><i class='fas fa-angle-right'></i></li>"
            sb += "<li class='last' onclick='PagingHelper.gotoPage(" + (_.data.totalPageCnt) +");'><i class='fas fa-angle-double-right'></i></li >"            
        }
        sb += "</ul>";
                    
        return sb;
    },
    "makeNum":function(className, content ){     //필요없음.    
        return "<li class='"+className+"''>["+content+"]</li>";
    },
    'setStartnumEndnum' : function() {
        // 시작 글번호
        this.data.startnum = (this.data.currentPage -1) * this.data.maxListCount + 1;

        // 마지막 글번호
        var tmp = this.data.currentPage * this.data.maxListCount;
        this.data.lastnum = (tmp > this.data.totalCnt?this.data.totalCnt:tmp);
    },
    'gotoPage':function(pageNum){
        console.log(pageNum);
                    
        this.data.currentPage = pageNum; //입력받은 페이지번호를 현재페이지로 설정
        this.setStartnumEndnum();    //입력받은 페이지의 startnum과 endnum구하기

        //콘솔 출력 (삭제)
        console.log(this.data.currentPage+"/"+this.data.startnum +"/"+this.data.lastnum);
        //alert(this.data.currentPage+"/"+this.data.startnum +"/"+this.data.lastnum);
        
        //리스트 불러오는 ajax호출
        //////////////////////////
        $("#paging").html(this.pagingHtml()); 
    }
}

//PagingHelper.data.totalCnt = 1001;

$(document).ready(function() {
    $("#paging").append(PagingHelper.pagingHtml(1001)); 
    //해당 영역에 페이징 문자열 출력 
    //class에대한 스타일 정의 필요.
});